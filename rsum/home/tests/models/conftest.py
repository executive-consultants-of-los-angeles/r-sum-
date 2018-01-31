"""pytest configuration module."""
import pytest

import rsum.loadapps

from home.models.profile import Profile
from home.models.section import Section
from home.models.skills import Skills

rsum.loadapps.main()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    return Profile


@pytest.fixture(scope="session")
def section():
    """Create a section for testing."""
    return Section


@pytest.fixture(scope="session")
def skills():
    """Create a Skills object."""
    return Skills
