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
        f.close()

    def test_check_sections(self):
        return None

    def test_save_abridged_cv(self):
        abridged = self.abridged
        cv = CV()
        cv_id = cv.save_cv(abridged, 'abridged', template='acecv')
        self.assertEqual(
            cv_id,
            list(CV.objects.filter(
                id=cv_id
            ).values_list(
                'id',
                flat=True
            ))[0]
        )


    def test_save_complete_cv(self):
        complete = self.complete
        cv = CV()
        cv_id = cv.save_cv(complete, 'complete', template='acecv')
        self.assertEqual(
            cv_id,
            list(CV.objects.filter(
                id=cv_id
            ).values_list(
                'id',
                flat=True
            ))[0]
        ) 

    def test_sort_sections(self): 
        return None


class CVGetsTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/complete.yml')
        self.complete = yaml.load(f.read())
        f.close

    def test_get_cv(self):
        return None

    def test_get_experience(self):
        return None

    def test_get_skills(self):
        return None
    
    def test_get_values(self):
        return None
