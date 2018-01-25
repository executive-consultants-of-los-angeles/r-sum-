# -*- coding: utf-8 -*-
"""Test case for home.views."""
import pytest
from django.test import Client
from django.urls import reverse

from home.models.profile import Profile
from export.models import ExportDocument


@pytest.mark.usefixtures('db')
def test_index(export_document, profile):
    """Get the index and test some things."""
    client = Client()
    profile.create()
    response = client.get(reverse('docx'))

    if response.status_code != 200:
        raise AssertionError()

    if not isinstance(profile, Profile):
        raise AssertionError()

    if not isinstance(export_document, ExportDocument):
        raise AssertionError()
