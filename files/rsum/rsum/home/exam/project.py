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


class ProjectTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        abridged = yaml.load(f.read())
        f.close()

        cv = CV()
        cv.name = 'abridged'
        cv.save()

        for name, section in sorted(
            abridged.items(),
            key=lambda t: t[1].get('id')
        ): 
            if isinstance(section, str):
                pass
            else:
                s = Section()
                s.cv = cv
                s.name = name
                s.content = type(section)
                s.save()
                ss = SubSection()
                ss.name = 'ptest'
                ss.section = s
                ss.save()
                self.ss = ss

    def test_save_projects(self):
        ss = self.ss
        projects = {}
        projects.update({
            'projectthefirst': {
                'thisproject': 'values!',
            }
        })
        projects.update({
            'projectthesecond': {
                'dict': 'indeed',
            }
        })

        p = Project()
        
        for name, item in projects.iteritems():
            p_result = p.save_projects(item, ss, name)
            self.assertEqual(
                list(p_result),
                list(Project.objects.values())
            )

        projects = [
            'project',
            'list',
            'values'
        ]
        for item in projects:
            p_result = p.save_projects(item, ss, 'list')
            self.assertEqual(
                list(p_result),
                list(Project.objects.values())
            )

        projects = unicode('Unicode value.')
        p_result = p.save_projects(projects, ss, 'unicode')
        self.assertEqual(
            list(p_result),
            list(Project.objects.values())
        )

        projects = str('String value.')
        p_result = p.save_projects(projects, ss, 'string')
        self.assertEqual(
            list(p_result),
            list(Project.objects.values())
        )
