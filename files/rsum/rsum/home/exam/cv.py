#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV

import yaml


class CVTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/alex/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        f = open('/srv/rsum/cvs/alex/complete.yml')
        self.complete = yaml.load(f.read())
        f.close()

    def test_check_sections(self):
        cv = CV()
        self.cv_id = cv.check_sections(
            name_of_owner='alex',
            name_of_cv='complete', 
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
        cv = CV()
        cv_id = cv.check_sections(
            name_of_owner='alex',
            name_of_cv='complete',
            template='acecv'
        )
        self.complete_sections = cv.get_cv(cv_id=cv_id, cvname='complete').get('sections')
        self.skills = cv.get_skills({'cv':self.complete_sections})
        self.values = cv.get_values({'cv':self.complete_sections})
        self.experience = cv.get_experience({'cv':self.complete_sections})
        self.cv_id = cv_id 

        self.cv_abridged_id = cv.check_sections(
            name_of_owner='alex',
            name_of_cv='abridged',
            template='acecv'
        )
        self.ab_sections = cv.get_cv(cv_id=cv_id, cvname='abridged').get('sections')

    def test_get_cv(self):
        cv_instance = CV()
        complete_sections = cv_instance.get_cv(cv_id=self.cv_id, cvname='complete').get('sections')
        ab_sections = cv_instance.get_cv(cv_id=self.cv_abridged_id, cvname='abridged').get('sections')
        self.assertEqual(
            len(ab_sections),
            len(self.ab_sections)
        )
        self.assertEqual(
            len(complete_sections),
            len(self.complete_sections)
        )

    def test_get_experience(self):
        cv_instance = CV()
        context = {
            'cv': self.complete_sections
        }
        experience = cv_instance.get_experience(context)
        self.assertEqual(
            experience,
            self.experience
        )

    def test_get_skills(self):
        cv_instance = CV()
        context = {
            'cv': self.complete_sections
        }
        skills = cv_instance.get_skills(context)
        self.assertEqual(
           skills,
           self.skills
        )
    
    def test_get_values(self):
        cv_instance = CV()
        context = {
            'cv': self.complete_sections
        }
        values = cv_instance.get_values(context)
        self.assertEqual(
            values,
            self.values
        )
