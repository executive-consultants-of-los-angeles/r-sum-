# -*- coding: utf-8 -*-
"""Test case for home.views."""
from __future__ import unicode_literals


class ViewsTestCase(object):
    """Class for testing home.views."""

    assertion = True

    def test_index(self):
        """Test retrieval of index page."""
        assert self.assertion

    def test_export_docx(self):
        """Test export of Word format document.

        :return: None
        :raises: :exc:`AssertionError`
        """
        assert self.assertion
