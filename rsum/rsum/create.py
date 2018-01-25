"""Module creates database entries for a profile."""
from rsum import loadapps

from home.models.profile import Profile

loadapps.main()

Profile.create()
