"""Test module for export class."""
import pytest
from home.export.word import ExportDocument


def test_export(export_document):
    """Test the object."""
    print(export_document)
    if not isinstance(export_document, ExportDocument):
        raise AssertionError()


@pytest.mark.usefixtures('db')
def test_run_export(export_document):
    """Run the export method and see what happens."""
    print(export_document.export(1))
