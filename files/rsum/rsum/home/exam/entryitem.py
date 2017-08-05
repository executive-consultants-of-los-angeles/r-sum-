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
from home.schema.entryitem import EntryItem

import yaml


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
