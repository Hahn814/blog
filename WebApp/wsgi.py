"""
WSGI config for WebApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebApp.settings')
print('===== sys.path / PYTHONPATH =====')
for k in sorted(os.environ.keys()):
    v = os.environ[k]
    print('%-30s %s' % (k, v[:70]))

application = get_wsgi_application()
