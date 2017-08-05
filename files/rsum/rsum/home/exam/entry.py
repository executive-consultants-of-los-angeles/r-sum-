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

import yaml


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
