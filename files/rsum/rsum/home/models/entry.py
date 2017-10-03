#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for Entry objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from entryitem import EntryItem


class Entry(models.Model):
    """Class for Entry objects.

    :attribute project_item:
        Associated :obj:`home.models.project_item.ProjectItem` object.

    :attribute name: Name of stored content.
    :attribute content: Actual stored content.
    """
    project_item = models.ForeignKey(
        'home.ProjectItem',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True)
    content = models.TextField() 

    def get_entry(self, project_item):
        """Get an Entry object.
        
        :param project_item: Related ProjectItem object.
        :type project_item: :obj:`home.models.projectitem.ProjectItem`
        :return: List of associated Entry object values.
        :rtype: list(object)
        """
        entries = []
        for entry in list(
            Entry.objects.filter(
                project_item=project_item
            ).values()
        ):
            entry_item_instance = EntryItem()
            entry.update({
                'value': entry_item_instance.get_list_item(
                    Entry.objects.filter(
                        id=entry.get('id')
                    )
                )
            })
            entries.append(entry)
        return entries

    def save_entry(self, entry, project_item):
        """Save an Entry object.

        :param entry: Entry to be saved.
        :type entry: :obj:'`home.models.entry.Entry`
        :param project_item: Related :obj:`home.models.projectitem.ProjectItem` 
        :return: Dictionary containing the saved Entry values.
        :rtype: dict(str, str)
        """
        if isinstance(entry, dict):
            for k, v in entry.iteritems():
                entry_instance = Entry()
                entry_instance.project_item = project_item 
                entry_instance.name = k
                entry_instance.value = type(v)
                entry_instance.save()
                entry_item_instance = EntryItem()
                entry_item_instance.save_list_item(v, entry_instance)
            return Entry.objects.values() 

    class Meta:
        app_label = "home"
        managed = True
