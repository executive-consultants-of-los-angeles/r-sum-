#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project
from home.schema.projectitem import ProjectItem
from home.schema.entryitem import EntryItem
from home.schema.entry import Entry

import home
import yaml

home.CV = CV()
home.Section = Section()
home.SubSection = SubSection()
home.Project = Project()
home.ProjectItem = ProjectItem()
home.EntryItem = EntryItem()
home.Entry = Entry()

class CVTestCase(TestCase):
    def setUp(self):
        CV.objects.create(name='abridged', template='acecv')
        CV.objects.create(name='complete', template='acecv')

    def test_complete(self):
        complete = open('/srv/rsum/cvs/complete.yml')
        complete_dict = yaml.load(complete.read())
        cv = CV.objects.get(name='complete')
        self.assertEqual(cv.id,2)

    def test_abridged(self):
        cv = CV.objects.get(name='abridged')
        self.assertEqual(cv.id,1)

    def test_save_abridged_cv(self):
        abridged = open('/srv/rsum/cvs/abridged.yml')
        abridged_dict = yaml.load(abridged.read())
        abridged.close()
        abridged = abridged_dict
        cv = CV()
        cv_return = cv.save_cv(abridged, 'abridged', 'acecv')
        print(cv_return)
        cv = CV.objects.filter(
            name = 'abridged'
        )
        self.assertEqual(len(cv),2)
