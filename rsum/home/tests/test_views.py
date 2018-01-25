# -*- coding: utf-8 -*-
"""Test case for home.views."""
from django.test import Client
from django.urls import reverse


class TestViews(object):
    """Class for testing home.views."""

    assertion = True
    client = Client()

    def test_index(self):
        """Get the index and test some things."""
        response = self.client.get(reverse('main'))

        if response.status_code != 200:
            raise AssertionError()
