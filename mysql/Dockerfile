FROM mysql:8.0
ARG MY_UID
ARG MY_GID

# ユーザーIDとグループIDを指定して、新しいユーザーを作成します。
RUN groupadd -g $MY_GID mysqlgroup
RUN useradd -u $MY_UID -g $MY_GID -ms /bin/bash mysqluser

# 新しいユーザーにデータディレクトリの所有権を付与します。
#RUN chown -R mysqluser:mysql /var/lib/mysql

# 新しいユーザーで実行するように設定します。
USER mysqluser