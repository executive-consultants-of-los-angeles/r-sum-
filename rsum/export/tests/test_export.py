"""Test module for export class."""
import pytest

from home.models.profile import Profile
from home.export.word import ExportDocument


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
