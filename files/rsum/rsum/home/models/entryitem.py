#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module to define EntryItem objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models


class EntryItem(models.Model):
    """Class that defines EntryItem objects.
    
    :attribute entry: Related entry object. 
    :attribute name: Name of stored content.
    :attribute content: Stored content.
    """
    entry = models.ForeignKey('home.Entry', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='entry item')
    content = models.TextField() 

    def get_list_item(self, entry):
        """Get an EntryItem object.

        :param entry: The related Entry object.
        :type entry: obj:`home.models.entry.Entry`
        :return: List of EntryItem dictionaries.
        :rtype: list(obj:`home.models.entryitem.EntryItem`)
        """
        items = []
        for item in list(
            EntryItem.objects.filter(
                entry=entry
            ).values()
        ):
            items.append(item)
        return items

    def save_list_item(self, entry_item, entry):
        """Save an EntryItem object.
        
        :param entry_item: Content for current item.
        :type entry_item: str or list(str)
        :param entry: Related Entry object.
        :type entry: obj:`home.models.entry.Entry`
        :return: Dictionary of EntryItem values.
        :rtype: dict[str, str]
        """
        if (
            isinstance(entry_item, str) or
            isinstance(entry_item, unicode)
        ):
            entry_item_instance = EntryItem()
            entry_item_instance.entry = entry 
            entry_item_instance.value = entry_item 
            entry_item_instance.save()

        if isinstance(entry_item, list):
            for entry_item_value in entry_item:
                entry_item_instance = EntryItem()
                entry_item_instance.entry = entry 
                entry_item_instance.content = str(entry_item_value)
                entry_item_instance.save()
        return EntryItem.objects.values() 

    class Meta:
        app_label = "home"
        managed = True
