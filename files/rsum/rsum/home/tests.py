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


class SectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()

    def test_save_section(self):
        abridged = self.abridged
        cv = CV()
        cv.name = 'abridged'
        cv.template = 'acecv'
        cv.save()

        for name, section in sorted(
            abridged.items(),
            key=lambda t: t[1].get('id')
        ):
            section_instance = Section()
            section_result = section_instance.save_section(
                cv,
                section,
                name
            )
            self.assertEqual(
                list(Section.objects.values()),
                list(section_result)
            )


class SubSectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()

    def test_save_sub_section(self):
        abridged = self.abridged
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
                ss_result = ss.save_sub_sections(section, s)
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

        project_item.update({
            'string': 'this is a string'
        })

        pi = ProjectItem()
        pi_result = pi.save_project_item(project_item, self.p) 
        self.assertEqual(
            list(pi_result),
            list(ProjectItem.objects.values())
        )


class EntryTestCase(TestCase):
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


class EntryItemTestCase(TestCase):
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
                pi = ProjectItem()
                pi.content = type(dict())
                pi.project = p
                pi.save()
                e = Entry()
                e.content = type(list()) 
                e.projectitem = pi
                e.save()
                self.e = e

    def test_save_entry_item(self):
        e = self.e
        entry_item_string = str("this is a string")
        entry_item_list = [
            'this',
            'is',
            'a',
            'list',
            'of',
            'strings'
        ]

        ei = EntryItem()
        ei.entry = e
        ei.value = 'this is a different string'
        ei.save()

        ei = EntryItem()
        ei_result = ei.save_list_item(entry_item_string, e)
        self.assertEqual(
            list(ei_result),
            list(EntryItem.objects.values())
        )

        ei_result = ei.save_list_item(entry_item_list, e)
        self.assertEqual(
            list(ei_result),
            list(EntryItem.objects.values())
        )
