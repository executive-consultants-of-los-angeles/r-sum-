import django
from django.conf import settings

django.setup()

from home.models.profile import Profile

Profile.create('complete')
