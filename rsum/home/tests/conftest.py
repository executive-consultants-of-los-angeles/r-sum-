"""pytest configuration module."""
# pylint: disable=wrong-import-order
import pytest

import rsum.loadapps

from home.models.profile import Profile


rsum.loadapps.main()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    prof = Profile.create()
    return prof
