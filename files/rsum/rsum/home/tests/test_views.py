#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test case for home.views."""
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):
    """Class for testing home.views."""
    def setUp(self):
        """Setup test of index view."""
        self.client = Client()

    def test_index(self):
        """Method to retrieve index page.

        :return: None
        :raises: :exc:`AssertionError`
        """
        """
        client = self.client

        response = client.get(reverse('index'))
        self.assertEqual(
            response.status_code,
            200
        )
        """
        assert False

    def test_export_docx(self):
        """Test export of Word format document.

        :return: None
        :raises: :exc:`AssertionError`
        """
        assert False
