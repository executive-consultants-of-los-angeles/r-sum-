#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project
from home.schema.projectitem import ProjectItem
from home.schema.entry import Entry
from rsum.cv_settings import values as s

import yaml


class EntryTestCase(TestCase):
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
                p = Project()
                p.name = "pitest"
                p.content = type(dict())
                p.sub_section = ss
                p.save()
                pi = ProjectItem()
                pi.content = type(dict())
                pi.project = p
                pi.save()
                self.pi = pi


    def test_save_entry(self):
        entry = {}
        entry.update({
            'dictionary!': {
                'pictionary!': 'is',
                'a': 'game',
            },
            'that_i': {
                'never': 'played',
            }
        })

        e = Entry()
        e_result = e.save_entry(entry, self.pi)
        self.assertEqual(
            list(e_result),
            list(Entry.objects.values())
        )


class GetEntryTestCase(TestCase):
    def setUp(self):
        cv_instance = CV()
        cv_id = cv_instance.check_sections(name_of_owner='alex', name_of_cv='abridged', template='acecv')
        sections = Section.objects.filter(cv=cv_instance)
        subsections = [list(SubSection.objects.filter(section=section)) for section in sections]
        projects = []
        for subsection in subsections:
            for subsection_object in subsection:
                project = list(Project.objects.filter(
                    sub_section=subsection_object
                ))
                projects.append(project)
        projectitems = []
        for project in projects:
            for project_object in project:
                projectitem = list(ProjectItem.objects.filter(
                    project=project_object
                ))
                projectitems.append(projectitem)
        entry_instance = Entry()
        entries = []
        for projectitem in projectitems:
            for projectitem_object in projectitem:
                entries.append(entry_instance.get_entry(projectitem_object))
        self.entries = entries
        self.projectitems = projectitems
    
    def test_get_entry(self):
        entries = []
        entry_instance = Entry()
        for projectitem in self.projectitems:
            for projectitem_object in projectitem:
                entries.append(entry_instance.get_entry(projectitem_object))
        self.assertEqual(
            entries,
            self.entries
        )
