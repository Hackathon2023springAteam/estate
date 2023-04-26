FROM python:3.10.10-buster as builder
# FROM python:3.10.10-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir app
# コンテナ内で作業するディレクトリを /app に設定します。このコマンドを使用することで、以降のRUN、CMD、COPYなどのコマンドで使用するディレクトリを明示的に指定できます。また、Dockerイメージ内に /app ディレクトリがない場合は、自動的に作成されます。
WORKDIR /app
RUN mkdir -p tmp/sockets
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
# COPY . . は、Dockerイメージ内の作業ディレクトリ（WORKDIR で設定されたディレクトリ）から、同じDockerイメージ内の現在のディレクトリ（ . ）にファイルをコピーする
COPY . .


# runner
FROM python:3.10.10-slim-buster as production
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir app
WORKDIR /app
RUN mkdir -p tmp/sockets

RUN apt update \
    && apt install -y libpq5 libxml2 libmariadbclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=builder /app /app

# CMD uwsgi --ini uwsgi.ini
# uwsgi コマンドを実行し、uwsgi.ini ファイルを設定ファイルとして使用してWebサーバーを起動します。
CMD ["uwsgi", "--ini", "uwsgi.ini"]