"""Test module for export class."""
import pytest

from export.models import ExportDocument
from home.models.profile import Profile


def test_export(export_document):
    """Test the object."""
    if not isinstance(export_document, ExportDocument):
        raise AssertionError()


@pytest.mark.usefixtures('db')
def test_run_export(export_document, profile):
    """Run the export method and see what happens."""
    if not isinstance(profile, Profile):
        raise AssertionError()

    if not isinstance(export_document, ExportDocument):
        raise AssertionError()
