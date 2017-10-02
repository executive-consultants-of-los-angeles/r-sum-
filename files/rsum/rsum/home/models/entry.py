#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from entryitem import EntryItem


class Entry(models.Model):
    projectitem = models.ForeignKey(
        'home.ProjectItem',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True)
    content = models.TextField() 

    def get_entry(self, project_item):
        entries = []
        for entry in list(
            Entry.objects.filter(
                projectitem=project_item
            ).values()
        ):
            eli = EntryItem()
            entry.update({
                'value': eli.get_list_item(
                    Entry.objects.filter(
                        id=entry.get('id')
                    )
                )
            })
            entries.append(entry)
        return entries

    def save_entry(self, entry, pi_l):
        if isinstance(entry, dict):
            for k, v in entry.iteritems():
                pe_i = Entry()
                pe_i.projectitem = pi_l
                pe_i.name = k
                pe_i.value = type(v)
                pe_i.save()
                eli = EntryItem()
                eli.save_list_item(v, pe_i)
            return Entry.objects.values() 

    class Meta:
        app_label = "home"
        managed = True
