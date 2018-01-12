"""pytest configuration module."""
import pytest

import django

from home.models.profile import Profile

django.setup()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    test_profile = Profile.create()
    print(test_profile)
    return test_profile
