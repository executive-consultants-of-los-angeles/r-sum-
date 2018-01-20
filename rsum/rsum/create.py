"""Module creates database entries for a profile."""
import os
import tempfile
import loadapps

from home.models.profile import Profile

loadapps.main()

Profile.objects.filter(name=os.environ.get('RSUM_ENV')).delete()
Profile.create()

with tempfile.TemporaryFile() as tmpf:
    tmpf.write('ready')
