#!/bin/sh

# マイグレーションを実行
docker compose -f docker-compose.yml exec app python manage.py makemigrations RealEstate360 --noinput
docker compose -f docker-compose.yml exec app python manage.py migrate --noinput

# staticのファイルをsettings.pyで指定した場所に集める
docker compose -f docker-compose.yml exec app python manage.py collectstatic --noinput

# スーパーユーザー作成
# docker compose -f docker-compose.yml exec app python manage.py createsuperuser