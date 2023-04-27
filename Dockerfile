FROM python:3

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

# ユーザーを作成
ARG MY_UID
ARG MY_GID
RUN groupadd -g $MY_GID appuser && \
    useradd -u $MY_UID -g $MY_GID -m appuser \
    && echo "appuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

#ローカルと一致するUID,GIDのappuserでログイン
USER appuser
WORKDIR /home/appuser/app
ENV PATH="/home/appuser/.local/bin:${PATH}"
RUN pip install --upgrade pip && pip install --upgrade setuptools

# rootに変更
USER root
COPY --chown=appuser:appuser ./requirements.txt /home/appuser/app/requirements.txt
RUN pip install -r requirements.txt
# appuserに変更
USER appuser
# アプリケーションのコードをコピー
COPY --chown=appuser:appuser . /home/appuser/app
