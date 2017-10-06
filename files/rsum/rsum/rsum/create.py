import sys
import os
import socket
import django
from django.conf import settings

if socket.gethostname() == 'ecla.solutions':
    settings_mod = "rsum.settings"
else:
    settings_mod = "rsum.settings.{}".format(socket.gethostname())

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_mod)

django.setup()

from home.models.profile import Profile

Profile.create('complete')

f = open('/tmp/ready','w')
f.write('ready')
f.cloase()
