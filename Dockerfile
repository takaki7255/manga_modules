# python
FROM python:3.9

#作業ディレクトリ
WORKDIR /work

#パッケージのインストール
COPY requirements.txt ./
RUN pip install -U pip \
&& pip install --trusted-host pypi.python.org -r requirements.txt

#ファイルのコピー
COPY . .