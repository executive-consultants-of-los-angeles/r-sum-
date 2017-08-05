#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from home.schema.cv import CV

import home
import yaml

import home.views


class ViewsTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()

        f = open('/srv/rsum/cvs/complete.yml')
        self.complete = yaml.load(f.read())
        f.close

    def test_index(self):
        abridged = self.abridged
        cv = CV()

        client = Client()

        response = client.get(reverse('index'))
        print(response.status_code)
