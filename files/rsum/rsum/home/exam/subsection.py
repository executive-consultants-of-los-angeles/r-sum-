#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project

import home
import yaml

class SubSectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        abridged = self.abridged
        cv = CV()
        cv.name = 'abridged'
        cv.save()

        s = Section()
        s.cv = cv
        s.name = "test-subs"
        s.content = type(dict())
        s.save()
        self.s = s

    def test_save_sub_section(self):
        ss = SubSection()
        section = self.abridged.items()[3]

        ss_result = ss.save_sub_sections(section[1], self.s)
        for item in ss_result:
            try:
                self.assertEqual(
                    list(Project.objects.values()),
                    list(item)
                ) 
            except:
                self.assertEqual(
                    None,
                    item 
                ) 


class GetSubSectionTestCase(TestCase):
    def setUp(self):
        cv_instance = CV()
        cv_id = cv_instance.check_sections(cvname='abridged', template='acecv')
        sections = Section.objects.filter(
            cv = CV.objects.filter(
                id=cv_id
            )
        )
        subsection_instance = SubSection()
        subsections = [subsection_instance.get_sub_section(section) for section in sections]
        self.subsections = subsections
        self.sections = sections
    
    def test_get_subsection(self):
        subsection_instance = SubSection()
        subsections = [subsection_instance.get_sub_section(section) for section in self.sections]
        self.assertEqual(
            self.subsections,
            subsections
        )
