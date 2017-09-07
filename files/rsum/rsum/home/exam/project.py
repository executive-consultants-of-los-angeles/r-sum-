#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project
from rsum.cv_settings import values as s

import home
import yaml


class ProjectTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/{0}/{1}.yml'.format(s.get('dir'), s.get('name')))
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


class GetProjectTestCase(TestCase):
    def setUp(self):
        cv_instance = CV()
        cv_id = cv_instance.check_sections(name_of_owner='alex', name_of_cv='abridged', template='acecv')
        sections = Section.objects.filter(
            cv = CV.objects.filter(
                id=cv_id
            )
        )
        self.subsections = [list(SubSection.objects.filter(
            section=section
        )) for section in sections]
        self.projects = []
        project_instance = Project()
        for subsection in self.subsections:
            for subsection_object in subsection:
                self.projects.append(
                    project_instance.get_projects(subsection_object)
                )

    def test_get_project(self):
        project_instance = Project()
        projects = []
        for subsection in self.subsections:
            for subsection_object in subsection:
                projects.append(project_instance.get_projects(subsection_object))
        self.assertEqual(projects,self.projects) 
