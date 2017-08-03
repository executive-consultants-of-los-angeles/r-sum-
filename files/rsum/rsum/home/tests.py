#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.entryitem import EntryItem
from home.schema.entry import Entry

import home

home.Entry = Entry()

class EntryItemTestCase(TestCase):
    def setUp(self):
        EntryItem.objects.create(content="item")
    
    def test_entry_item(self):
        item = EntryItem.objects.get(content="item")
        self.assertEqual(item.content,'item')
