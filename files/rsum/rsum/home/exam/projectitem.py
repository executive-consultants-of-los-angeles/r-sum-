#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project
from home.schema.projectitem import ProjectItem

import home
import json
import yaml


class ProjectItemTestCase(TestCase):
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
                p = Project()
                p.name = "pitest"
                p.content = type(dict())
                p.sub_section = ss
                p.save()
                self.p = p

    def test_save_project_items(self):
        project_item = {}
        project_item.update({
            'dictionary': {
                'this': 'is',
                'a': 'dictionary',
            }
        })

        pi = ProjectItem()
        pi_result = pi.save_project_item(project_item, self.p) 
        self.assertEqual(
            list(pi_result),
            list(ProjectItem.objects.values())
        )

        project_item = str('this is a string')
        pi_result = pi.save_project_item(project_item, self.p)
        self.assertEqual(
            list(pi_result),
            list(ProjectItem.objects.values())
        )        
        
        project_item = unicode('this is a unicode')
        pi_result = pi.save_project_item(project_item, self.p)
        self.assertEqual(
            list(pi_result),
            list(ProjectItem.objects.values())
        )


class GetProjectItemTestCase(TestCase):
    def setUp(self):
        cv_instance = CV()
        cv_id = cv_instance.check_sections(cvname='abridged', template='acecv')
        sections = Section.objects.filter(cv=cv_instance)
        subsections = [list(SubSection.objects.filter(section=section)) for section in sections] 
        self.projects = []
        for subsection in subsections:
            for subsection_object in subsection:
                project = list(Project.objects.filter(
                    sub_section=subsection_object
                ))
                self.projects.append(project)
        self.projectitems = []
        for project in self.projects:
            for project_object in project:
                projectitem_instance = ProjectItem()
                projectitem = projectitem_instance.get_project_item(project_object)
                self.projectitems.append(projectitem)

    def test_get_project_item(self):
        projectitems = []
        for project in self.projects:
            for project_object in project:
                projectitem_instance = ProjectItem()
                projectitem = projectitem_instance.get_project_item(project_object)
                projectitems.append(projectitem)
        self.assertEqual(
            self.projectitems,
            projectitems
        )
