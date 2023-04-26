# Mucha_La_Hetta

1. docker-compose.ymlと同じ階層と、djangoディレクトリの中に２つ開発環境「.env」ファイルを作成し記述する。

2. 下記コマンドを実行する
```
docker compose -f docker-compose.yml up -d
```
* ブラウザで確認
http://localhost

3. マイグレートして、スーパーユーザーを作成する
```
./.migration.sh

docker compose -f docker-compose.yml exec app python manage.py createsuperuser
```
* ブラウザで確認
http://localhost/admin


4. 一旦Dockerをリセットする
```
./.docker_clear.sh
```

5. Dockerを起動
```
docker compose -f docker-compose.yml up -d --build
```

※requirements.txtは二つありますが、エクスプローラーの一番下のrequirements.txtに開発中は記述してください。
