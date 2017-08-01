#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models

class Entry(models.Model):
    project_item = models.ForeignKey('home.ProjectItem', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    value = models.CharField(max_length=200, null = True) 

    def get_entry(self, project_item):
        entries = []
        for entry in list(
            Entry.objects.filter(
                project_item_list = project_item
            ).values()
        ):
            eli = EntryListItem()
            entry.update({
                'value': eli.get_list_item(
                    Entry.objects.filter(
                        id = entry.get('id') 
                    )
                ) 
            })
            entries.append(entry)
        return entries

    def save_entry(self, entry, pi_l):
        if type(entry) == type(dict()):
            for k, v in entry.iteritems():
                pe_i = Entry()
                pe_i.project_item_list = pi_l
                pe_i.name = k
                pe_i.value = type(v)
                pe_i.save()
                eli = EntryListItem()
                eli.save_list_item(v, pe_i)
            return pe_i 

    class Meta:
        app_label = "home"
