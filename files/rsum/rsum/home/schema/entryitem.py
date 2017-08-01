#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from home.schema.entry import Entry

class EntryItem(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, null=True)
    
    def get_list_item(self, entry):
        items = []
        for item in list(
            EntryItem.objects.filter(
                entry = entry
            ).values()
        ):
            items.append(item)
        return items
            

    def save_list_item(self, list_item, pe):
        if type(list_item) == type(list()):
            for i in list_item:
                eli = EntryItem()
                eli.entry = pe
                eli.value = i
                eli.save()
            return eli 

        if type(list_item) == type(str()):
            eli = EntryItem()
            eli.entry = pe
            eli.value = list_item
            eli.save()
        return eli
