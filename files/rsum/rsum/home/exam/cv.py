#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV

import yaml


class CVTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        f = open('/srv/rsum/cvs/complete.yml')
        self.complete = yaml.load(f.read())
        f.close

    def test_save_abridged_cv(self):
        abridged = self.abridged
        cv = CV()
        result = cv.save_cv(abridged, 'abridged', template='acecv')

        self.assertEqual(result.name, 'abridged')
        self.assertEqual(result.template, 'acecv')

    def test_save_complete_cv(self):
        complete = self.complete
        cv = CV()
        result = cv.save_cv(complete, 'complete', template='acecv')
    
        self.assertEqual(result.name, 'complete')
        self.assertEqual(result.template, 'acecv')
