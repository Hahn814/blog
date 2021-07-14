# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/WebApp

COPY . /opt/app/WebApp
WORKDIR /opt/app/WebApp

RUN curl -sLk https://github.com/sass/dart-sass/releases/download/1.22.7/dart-sass-1.22.7-linux-x64.tar.gz -o sass.tar.gz
RUN tar xvfz sass.tar.gz && rm sass.tar.gz
RUN dart-sass/sass --no-source-map /opt/app/WebApp/blog/static/scss/app.scss /opt/app/WebApp/blog/static/css/app.css

WORKDIR /opt/app/
RUN pip install -r WebApp/requirements/base.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
