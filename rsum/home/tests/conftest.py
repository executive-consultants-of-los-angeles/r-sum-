"""pytest configuration module."""
# pylint: disable=wrong-import-order
import pytest

from . import loadapps

from home.models.profile import Profile


loadapps.main()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    prof = Profile.create()
    print(prof)
    return prof
