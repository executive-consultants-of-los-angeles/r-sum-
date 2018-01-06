"""Module creates database entries for a profile."""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsum.settings")
import django
django.setup()
from home.models.profile import Profile

Profile.create()

with open('/tmp/ready', 'w') as ready:
    ready.write('ready')
    ready.close()
