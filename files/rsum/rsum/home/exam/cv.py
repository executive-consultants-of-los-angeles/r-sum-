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
        cv = CV()
        self.cv_id = cv.check_sections(
            cvname='complete', 
            template='acecb'
        )
        self.assertEqual(
            self.cv_id,
            list(CV.objects.filter(
                id=self.cv_id
            ).values_list(
                'id',
                flat=True
            ))[0] 
        )

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


class CVGetsTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/complete.yml')
        self.complete = yaml.load(f.read())
        f.close()
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        cv = CV()
        cv_id = cv.check_sections(
            cvname='complete',
            template='acecv'
        )
        self.complete_sections = cv.get_cv(cv_id=cv_id, cvname='complete')
        self.complete_sorted = cv.sort_sections(self.complete_sections)
        self.skills = cv.get_skills({'cv':self.complete_sorted})
        self.cv_id = cv_id 

    def test_get_cv(self):
        cv_instance = CV()
        complete_sections = cv_instance.get_cv(cv_id=self.cv_id, cvname='complete')
        self.assertEqual(
            complete_sections,
            self.complete_sections
        )

    def test_get_experience(self):
        return None

    def test_get_skills(self):
        cv_instance = CV()
        context = {
            'cv': self.complete_sorted
        }
        skills = cv_instance.get_skills(context)
        self.assertEqual(
            skills,
            self.skills
        )
    
    def test_get_values(self):
        return None

    def test_sort_sections(self): 
        cv_instance = CV()
        cv = cv_instance.get_cv(cv_id=self.cv_id)
        sections = cv_instance.sort_sections(cv) 
        self.assertEqual(
            sections,
            self.complete_sorted
        )
