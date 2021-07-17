#!/bin/sh
# start-server.sh

set -x

cd /opt/app/WebApp

python manage.py collectstatic --clear --no-input
python manage.py migrate --no-input 

gunicorn --config python:WebApp.conf.gunicorn_conf WebApp.wsgi:application