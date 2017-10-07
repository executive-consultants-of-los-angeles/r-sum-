"""WSGI config for rsum project."""
import os
import socket

settings = "rsum.settings.{}".format(socket.gethostname())

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
