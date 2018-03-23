"""Conftest config for pytest."""
import pytest
import rsum.loadapps

from export.models import ExportDocument
from home.models.profile import Profile

rsum.loadapps.main()


@pytest.fixture(scope="session")
def profile():
    """Create a profile for testing."""
    prof = Profile.create()
    return prof


@pytest.fixture(scope="session")
def export_document():
    """Return a DB object."""
    return ExportDocument()
