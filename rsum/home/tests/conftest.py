"""pytest configuration module."""
import pytest

import django
from django.conf import settings

from home import models
from home.export.word import ExportDocument

django.setup()



@pytest.fixture(scope="session")
def export_document():
    """Return a DB object."""
    return ExportDocument()
