#!/bin/bash
source .env

docker-compose -f "docker-compose.yml" up -d --build db phpmyadmin
sleep 3
docker-compose -f "docker-compose.yml" up -d --build django
sleep 3

sudo chown ${MY_UID}:${MY_GID} ./${MY_PROJECT}
rm -rf ./${MY_PROJECT}

# localhostからdjangoのプロジェクトとアプリケーションを生成
docker-compose exec django django-admin startproject ${MY_PROJECT}
docker-compose exec django sh -c "cd ${MY_PROJECT} && python manage.py startapp ${MY_APPLICATION}"

# MySQLを使うようにlocalhostからdjangoコンテナのsetting.pyを更新
# デフォルトのDATABASES={}を削除し、setting.pyの末尾にDATABASES={}を1行ずつ挿入
SETTINGS_FILE="/home/appuser/app/${MY_PROJECT}/${MY_PROJECT}/settings.py"
docker-compose exec django sh -c "\
  sed -i.bak '/DATABASES = {/,/^}/d' $SETTINGS_FILE && \
  echo \"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${MYSQL_DATABASE}',
        'USER': '${MYSQL_USER}',
        'PASSWORD': '${MYSQL_PASSWORD}',
        'HOST': '${MYSQL_HOST}',
        'PORT': '${MYSQL_PORT}',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}\" >> $SETTINGS_FILE && \
  rm $SETTINGS_FILE.bak"