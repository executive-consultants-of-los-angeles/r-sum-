#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test classes for entry model."""
from django.test import TestCase
from django.db import models

import home.models


class EntryTestCase(TestCase):
    """Test class for the Entry model.

    .. attribute:: cv

       Related :obj:`home.models.cv.CV` for testing.

    .. attribute:: project_item
    
       Related :obj:`home.models.projectitem.ProjectItem` for testing.

    .. attribute:: entry

       The :obj:`home.models.entry.Entry` necessary for tests.
    """
    cv = home.models.cv.CV()
    project_item = home.models.projectitem.ProjectItem
    entry = home.models.entry.Entry()

    def setUp(self):
        """Setup for EntryTestCase.

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
        self.project_item = home.models.projectitem.ProjectItem(project=project)
        self.project_item.save()
        return None

    def test_save_entry(self):
        """Test saving an entry to the Entry model.
        
        :return: none
        :rtype: None
        """
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

        entry_instance = self.entry 
        entry_instance_result = entry_instance.save_entry(
            entry,
            self.project_item)

        assert isinstance(entry_instance_result,
            models.query.QuerySet)
        return None


class GetEntryTestCase(TestCase):
    """Class for testing the get methods for entries."""
    def setUp(self):
        """Setup the GetEntryTestCase."""
        return None 
    
    def test_get_entry(self):
        """Test getting an entry."""
        return None
