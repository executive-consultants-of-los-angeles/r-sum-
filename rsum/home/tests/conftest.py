"""pytest configuration module."""
import django
import pytest

from home.export.word import ExportDocument


django.setup()


@pytest.fixture(scope="session")
def export_document():
    """Return a DB object."""
    return ExportDocument()
