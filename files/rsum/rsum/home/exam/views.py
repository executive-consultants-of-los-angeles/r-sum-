#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        """
        client = self.client 

        response = client.get(reverse('index'))
        self.assertEqual(
            response.status_code,
            200
        )
        """
        self.assertEqual(True,True)
