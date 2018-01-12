"""pytest configuration module."""
import pytest

from home.export.word import ExportDocument


@pytest.fixture(scope="session")
def export_document():
    """Return a DB object."""
    return ExportDocument()
