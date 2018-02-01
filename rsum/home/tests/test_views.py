# -*- coding: utf-8 -*-
"""Test case for home.views."""
import pytest
from django.test import Client
from django.urls import reverse

from home.models.profile import Profile


@pytest.mark.usefixtures('db')
def test_index(profile):
    """Get the index and test some things."""
    client = Client()
    response = client.get(reverse('main'))

    if response.status_code != 200:
        raise AssertionError()

    if not isinstance(profile, Profile):
        raise AssertionError()
