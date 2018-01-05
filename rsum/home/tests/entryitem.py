#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test class for the entry item test case."""
from django.test import TestCase
from django.db import models

import home.models


class EntryItemTestCase(TestCase):
    """EntryItemTestCase class.
        
    .. attribute:: cv 

       The instantiated :obj:`home.models.cv.CV` object for the
       current :obj:`home.models.entryitem.EntryItem`.

    .. attribute:: entry

       The :obj:`home.models.entry.Entry` necessary for tests.

    .. attribute:: entry_item

       The :obj:`home.models.entryitem.EntryItem` Model for testing.
    """
    cv = home.models.cv.CV()
    entry = home.models.entry.Entry
    entry_itemm = home.models.entryitem.EntryItem

    def setUp(self):
        """Setup the EntryItemTestCase.
        
        :return: none
        :rtype: None
        """
        cv_id = self.cv.check_sections() 
        cv = home.models.cv.CV(id=cv_id)
        section = home.models.section.Section(cv=cv)
        section.save()
        sub_section = home.models.subsection.SubSection(section=section)
        sub_section.save()
        project = home.models.project.Project(sub_section=sub_section)
        project.save()
        project_item = home.models.projectitem.ProjectItem(project=project)
        project_item.save()
        self.entry = home.models.entry.Entry(project_item=project_item)
        self.entry.save()
        self.entry_item = home.models.entryitem.EntryItem()
        return None


    def test_save_entry_item(self, entry=home.models.entry.Entry):
        """EntryItem objects should save corrrectly.

        :param entry: The :obj:`home.models.entry.Entry` related to
            the current :obj:`home.models.entry.EntryItem` being tested.
        :type entry: :obj:`home.models.entry.Entry`
        :return: none 
        :rtype: None 
        """
        entry_item_string = str("this is a string")
        entry_item_instance = self.entry_item 
        entry_item_instance.name = "Testing."
        entry_item_instance.content = entry_item_string
        entry_item_instance.entry = self.entry
        entry_item_instance.save()

        assert isinstance(
            entry_item_instance, 
            home.models.entryitem.EntryItem)
        return None

    def test_save_entry_string(self, entry=home.models.entry.Entry):
        """Test saving a string.

        :param entry: The :obj:`home.models.entry.Entry` related to
            the current :obj:`home.models.entry.EntryItem` being tested.
        :type entry: :obj:`home.models.entry.Entry`
        :return: none 
        :rtype: None 
        """
        entry_item_string = str("this is a string")

        test_save_entry_item = self.entry_item.save_entry_item(
            entry_item_list,
            self.entry)

        assert isinstance(
            test_save_entry_item,
            models.query.QuerySet)
        return None

    def test_save_entry_list(self, entry=home.models.entry.Entry):
        """Test saving a list.

        :param entry: The :obj:`home.models.entry.Entry` related to
            the current :obj:`home.models.entry.EntryItem` being tested.
        :type entry: :obj:`home.models.entry.Entry`
        :return: none 
        :rtype: None 
        """
        entry_item_list = [
            'this',
            'is',
            'a',
            'list',
            'of',
            'strings'
        ]

        test_save_entry_item = self.entry_item.save_entry_item(
            entry_item_list,
            self.entry) 

        assert isinstance(
            test_save_entry_item,
            models.query.QuerySet)
        return None


class GetEntryItemTestCase(TestCase):
    """Test class for EntryItem get methods."""
    def setUp(self):
        """Setup testing for EntryItem get methods.
        
        :return: none
        :rtype: None
        """
        return None

    def test_get_entry_item(self):
        """Test getting an EntryItem. 
        
        :return: none
        :rtype: None
        """
        return None
