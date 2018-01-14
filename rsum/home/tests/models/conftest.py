"""pytest configuration module."""
import pytest

import django

from home.models.profile import Profile
from home.models.section import Section

django.setup()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    return Profile


@pytest.fixture(scope="session")
def section():
    """Create a section for testing."""
    return Section
