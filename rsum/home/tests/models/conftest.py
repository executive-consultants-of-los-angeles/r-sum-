"""pytest configuration module."""
import pytest

from rsum import loadapps

from home.models.profile import Profile
from home.models.section import Section

loadapps.main()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    return Profile


@pytest.fixture(scope="session")
def section():
    """Create a section for testing."""
    return Section
