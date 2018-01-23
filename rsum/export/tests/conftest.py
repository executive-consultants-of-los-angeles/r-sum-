"""Conftest config for pytest."""
import pytest
from rsum import loadapps

from export.models import ExportDocument

loadapps.main()


@pytest.fixture(scope="session")
def export_document():
    """Return a DB object."""
    return ExportDocument()
