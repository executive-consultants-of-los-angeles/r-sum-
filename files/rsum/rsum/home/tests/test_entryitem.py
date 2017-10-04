#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test class for the entry item test case."""
from __future__ import unicode_literals
from __future__ import print_function

import socket
import yaml

from django.test import TestCase
from django.apps import apps

import home.models


class EntryItemTestCase(TestCase):
    """EntryItemTestCase class.
        
    .. attribute:: entry_instance

       The instantiated :obj:`home.models.entry.Entry` object for the
       current :obj:`home.models.entryitem.EntryItem`.

    .. attribute:: entry_item

       The :obj:`home.models.entryitem.EntryItem` Model for testing.
    """
    def setUp(self):
        """Setup the EntryItemTestCase.
        
        :return: none
        :rtype: None
        """
        self.entry_item = home.models.entryitem.EntryItem()
        self.entry_instance = home.models.entry.Entry.create(
            name="test",
            content="none",
            project_item_id=1)


    def test_save_entry_item(self, entry=home.models.entry.Entry):
        """EntryItem objects should save corrrectly.  Test for the ability
           to save both strings and lists.

        :param entry: The :obj:`home.models.entry.Entry` related to
            the current :obj:`home.models.entry.EntryItem` being tested.
        :type entry: :obj:`home.models.entry.Entry`
        :return: True on success, False on failure.
        :rtype: bool
        """
        entry_item_string = str("this is a string")
        entry_item_list = [
            'this',
            'is',
            'a',
            'list',
            'of',
            'strings'
        ]

        entry_item_instance = self.entry_item 
        entry_item_instance.name = "Testing."
        entry_item_instance.content = entry_item_string
        entry_item_instance.entry = self.entry_instance
        entry_item_instance.save()

        print(type(entry_item_instance))
        return None


class GetEntryItemTestCase(TestCase):
    """Test class for EntryItem get methods."""
    def setUp(self):
        """Setup testing for EntryItem get methods."""
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
        entries = []
        for projectitem in projectitems:
            for projectitem_object in projectitem:
                entry = list(Entry.objects.filter(
                    projectitem=projectitem_object
                ))
                entries.append(entry)
        entryitems = []
        for index,entry in enumerate(entries):
            entryitem = list(EntryItem.objects.filter(
                entry=index
            ))
            entryitems.append(entryitem)
        self.entryitems = entryitems
        self.entries = entries

    def test_get_entry_item(self):
        """Test getting an EntryItem. """
        entries = self.entries
        entryitems = []
        for index, entry in enumerate(entries):
            entryitem = list(EntryItem.objects.filter(
                entry=index
            ))
            entryitems.append(entryitem)
        self.assertEqual(
            self.entryitems,
            entryitems
        )
