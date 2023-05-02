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

./.docker_clear.sh を実行し、コンテナが破棄されると
次回の docker compose -f docker-compose.yml up -d --build は
./volumes のアクセス権限ミスマッチで止まってしまう。
./volumes を sudo rm -rf で削除するとコンテナが再作成されるが、
django のスーパーユーザーが消えてしまう

volumes/の ./nginx/static:/app/static 　によって docker コンテナに 2 つの style.css が発生してしまう。そのため.migration.sh の
docker compose -f docker-compose.yml exec app python manage.py collectstatic --noinput
で style.css の競合が発生しているとの警告が表示される。
回避するには
1.static フォルダを内部 volumes:を介して接続し、コンテナ内だけで完結させる。ただしコンテナ生成の度に collectstatic を実行する必要あり。
2.nginx はホットスワップが出来ないので、nginx 起動用のシェルスクリプトを作り static のコピーと起動を纏める。

dev コンテナで開発したかったので、docker-compose.yml の app に- ./django:/app を追加し、localhost の django フォルダと
django コンテナを接続した。
