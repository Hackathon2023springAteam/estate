# estate

- .env をルートフォルダに置く

- 最小構成プロジェクトのルートフォルダでターミナルを起動。
  最小構成プロジェクト
  .
  ├── [drwxrwxr-x USER USER] .devcontainer
  │ ├── [-rw-rw-r-- USER USER] devcontainer.json
  │ └── [-rw-rw-r-- USER USER] docker-compose.yml
  ├── [drwxrwxr-x USER USER] .vscode
  │ └── [-rw-rw-r-- USER USER] settings.json
  ├── [drwxrwxr-x USER USER] mysql
  │ ├── [drwxrwxr-x USER USER] data
  │ │ └── [drwxrwxr-x USER USER] db
  │ ├── [-rw-rw-r-- USER USER] Dockerfile
  │ └── [-rw-rw-r-- USER USER] my.cnf
  ├── [drwxrwxr-x USER USER] nginx
  │ └── [-rw-rw-r-- USER USER] nginx.conf
  ├── [-rw-rw-r-- USER USER] .env
  ├── [-rw-rw-r-- USER USER] .gitignore
  ├── [-rw-rw-r-- USER USER] Dockerfile
  ├── [-rw-rw-r-- USER USER] README.md
  ├── [-rwxrwxr-x USER USER] build_containers.sh
  ├── [-rw-rw-r-- USER USER] docker-compose.yml
  ├── [-rw-rw-r-- USER USER] requirements.txt
  └── [-rwxrwxr-x USER USER] start_containers.sh
- $ ./build_containers.sh を実行。
  django プロジェクト MY_PROJECT とアプリケーション MY_APPLICATION のフォルダが追加
  今回は hackathon_a と estate
  .
  ├── [drwxrwxr-x USER USER] .devcontainer
  │ ├── [-rw-rw-r-- USER USER] devcontainer.json
  │ └── [-rw-rw-r-- USER USER] docker-compose.yml
  ├── [drwxrwxr-x USER USER] .vscode
  │ └── [-rw-rw-r-- USER USER] settings.json
  ├── [drwxr-xr-x USER USER] MY_PROJECT
  │ ├── [drwxr-xr-x USER USER] MY_PROJECT
  │ │ ├── [-rw-r--r-- USER USER] **init**.py
  │ │ ├── [-rw-r--r-- USER USER] asgi.py
  │ │ ├── [-rw-r--r-- USER USER] settings.py
  │ │ ├── [-rw-r--r-- USER USER] urls.py
  │ │ └── [-rw-r--r-- USER USER] wsgi.py
  │ ├── [drwxr-xr-x USER USER] MY_APPLICATION
  │ │ ├── [drwxr-xr-x USER USER] migrations
  │ │ │ └── [-rw-r--r-- USER USER] **init**.py
  │ │ ├── [-rw-r--r-- USER USER] **init**.py
  │ │ ├── [-rw-r--r-- USER USER] admin.py
  │ │ ├── [-rw-r--r-- USER USER] apps.py
  │ │ ├── [-rw-r--r-- USER USER] models.py
  │ │ ├── [-rw-r--r-- USER USER] tests.py
  │ │ └── [-rw-r--r-- USER USER] views.py
  │ └── [-rwxr-xr-x USER USER] manage.py
  ├── [drwxrwxr-x USER USER] mysql
  │ ├── [drwxrwxr-x USER USER] data
  │ │ └── [drwxrwxr-x USER USER] db
  │ │ └── dictionaries & files
  ├── [drwxrwxr-x USER USER] nginx
  │ ├── [drwxr-xr-x root root ] static
  │ └── [-rw-rw-r-- USER USER] nginx.conf
  ├── [drwxr-xr-x root root ] phpmyadmin
  │ └── [drwxr-xr-x root root ] sessions
  ├── [-rw-rw-r-- USER USER] .env
  ├── [-rw-rw-r-- USER USER] .gitignore
  ├── [-rw-rw-r-- USER USER] Dockerfile
  ├── [-rw-rw-r-- USER USER] README.md
  ├── [-rwxrwxr-x USER USER] build_containers.sh
  ├── [-rw-rw-r-- USER USER] docker-compose.yml
  ├── [-rw-rw-r-- USER USER] requirements.txt
  └── [-rwxrwxr-x USER USER] start_containers.sh

- django の中に MY_PROJECT/MY_PROJECT と MY_PROJECT/MY_APPLICATION が生成される。

- .env にて MY_PROJECT=hackathon_a と MY_APPLICATION=mucha_la_hetta が宣言されている。

- phpmyadmin ディレクトリが root:root で自動生成される。

- nginx/static ディレクトリが root:root で自動生成される。

- nginx はホットスワップができないため、最終盤にて nginx コンテナ生成する必要がある。
  そこで build_containers.sh と start_containers.sh に分離した。

- ./build_containers.sh → MY_APPLICATION の Dev Container に入って開発 → Dev Container から出て./start_containers.sh の流れ。

- localhost に python がインストールされていれば、そのまま開発可能。ただしコンテナは requirements.txt に基づくため環境差が生じる。

- .env の MODE_ENV で development と production に切り替える。

- development の場合、build_containers.sh -> start_containers.sh で django の runserver が起動。
  localhost:5000 でブラウザ起動

- production の場合、build_containers.sh -> django プロジェクト編集 ->start_containers.sh で
  uWSGI+Nginx が起動。setting.py の ALLOWED_HOSTS = ['*'] を忘れない。
  最終的にはデプロイしたグローバル IP を記入。
  localhost でブラウザ起動

- 以降、生成コンテナが動作中でも build_containers.sh と start_containers.sh はそのまま実行できるが
  build_containers.sh を実行すると django プロジェクトが初期化されるので注意。

注記

- VSCode Reopen in container で Dev Container を初めて開き、そのまま local に戻ると
  .devcontainer が生成される。しかし所望のディレクトリではないので手動で変更している。
  .devcontaner/devcontainer.json の"workspaceFolder"を"/home/appuser/app" に変更。appuser は Dockerfile で生成されている。
  .devcontainer/docker-compose.yml の volumes:をコメントアウト。
