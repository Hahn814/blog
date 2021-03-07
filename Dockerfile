# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/WebApp
COPY start-server.sh /opt/app/
COPY . /opt/app/WebApp

WORKDIR /opt/app/WebApp
RUN curl -sLk https://github.com/sass/dart-sass/releases/download/1.22.7/dart-sass-1.22.7-linux-x64.tar.gz -o sass.tar.gz
RUN tar xvfz sass.tar.gz && rm sass.tar.gz
RUN dart-sass/sass --no-source-map /opt/app/WebApp/blog/static/scss/app.scss /opt/app/WebApp/blog/static/css/app.css

WORKDIR /opt/app/
RUN ls -lta
RUN pip install -r WebApp/requirements/base.txt
RUN chown -R www-data:www-data /opt/app

WORKDIR /opt/app/WebApp/

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]