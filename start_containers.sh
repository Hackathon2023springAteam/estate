#!/bin/bash

# コンテナを起動する関数
start_container_if_stopped() {
  container_name="$1"

  container_info=$(docker ps -a --format "{{.ID}}\t{{.Names}}\t{{.Status}}" | grep "$container_name")

  if [ -z "$container_info" ]; then
    echo "Container not found: $container_name"
    return 1
  fi

  container_id=$(echo "$container_info" | awk '{print $1}')
  container_status=$(echo "$container_info" | awk '{print $3}')

  if [ "$container_status" = "Exited" ]; then
    echo "Starting container: $container_id"
    docker start "$container_id"
  else
    echo "Container is already running: $container_id"
  fi
}

# コンテナ名を指定して関数を呼び出す
start_container_if_stopped "MySQL"
start_container_if_stopped "phpmyadmin"
start_container_if_stopped "django"

#環境変数によってNginxの有無、アクセスするポート番号を切り替える。
source .env
if [ "${MODE_ENV}" = "development" ]; then
  docker-compose exec django sh -c "cd ${MY_PROJECT} && python manage.py runserver 0.0.0.0:5000"
elif [ "${MODE_ENV}" = "production" ]; then
  docker-compose -f "docker-compose.yml" up -d --build nginx
  docker-compose exec django sh -c "cd ${MY_PROJECT} && uwsgi --socket :8000 --module ${MY_PROJECT}.wsgi:application"
else
  echo "Unknown MODE_ENV value: ${MODE_ENV}"
  exit 1
fi

