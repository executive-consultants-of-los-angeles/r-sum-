"""Module creates database entries for a profile."""
import tempfile
import loadapps

from home.models.profile import Profile

loadapps.main()

Profile.objects.delete()
Profile.create()

with tempfile.TemporaryFile() as tmpf:
    tmpf.write('ready')
