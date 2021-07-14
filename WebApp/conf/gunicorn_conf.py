import os

bind = "0.0.0.0:{WEB_PORT}".format(
    WEB_PORT=os.environ.get('WEB_PORT', 8020)
)

reload = True
proxy_allow_ips = "nginx"
workers = 4
loglevel = "debug"
wsgi_app = "WebApp.wsgi:application"