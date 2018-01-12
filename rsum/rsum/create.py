"""Module creates database entries for a profile."""
import tempfile
import django

from home.models.profile import Profile

django.setup()

Profile.create()

with tempfile.TemporaryFile() as tmpf:
    tmpf.write('ready')
