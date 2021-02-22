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

WORKDIR /opt/app/WebApp/
RUN python manage.py collectstatic

WORKDIR /opt/app/
RUN ls -lta
RUN pip install -r WebApp/requirements/base.txt
RUN chown -R www-data:www-data /opt/app


EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]