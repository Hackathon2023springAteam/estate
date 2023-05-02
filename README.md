# estate

1. docker-compose.yml と同じ階層と、django ディレクトリの中に２つ開発環境「.env」ファイルを作成し記述する。

2. 下記コマンドを実行する

```
docker compose -f docker-compose.yml up -d
```

- ブラウザで確認
  http://localhost

3. マイグレートして、スーパーユーザーを作成する

```
./.migration.sh

docker compose -f docker-compose.yml exec app python manage.py createsuperuser
```

- ブラウザで確認
  http://localhost/admin

4. 一旦 Docker をリセットする

```
./.docker_clear.sh
```

5. Docker を起動

```
docker compose -f docker-compose.yml up -d --build
```
