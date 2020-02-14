FROM python:3.7-alpine
RUN pip install --upgrade setuptools
RUN pip install mysql-connector-python
# ここから下はクローリングのためのライブラリのインストール
RUN apk --no-cache add gcc libc-dev libxml2-dev libxslt-dev
RUN pip install Requests
RUN pip install lxml
RUN pip install cssselect