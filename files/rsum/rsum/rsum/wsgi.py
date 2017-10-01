"""WSGI config for rsum project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsum.settings")

application = get_wsgi_application()
