#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from entry import Entry

class ProjectItem(models.Model):
    project = models.ForeignKey('home.Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null = True) 
    iterable = models.BooleanField(default=False)

    def get_project_item(self, project):
        project_item = []
        for project_item in list(
            ProjectItem.objects.filter(
                project = project
            ).values()
        ):
            if project_item.get('value') == u"<type 'dict'>":
                pe = Entry()
                project_item.update({
                    'value': pe.get_entry(
                        ProjectItem.objects.filter(
                            id = project_item.get('id')
                        )
                    )
                })        
                project_item.append(project_item)
            else:
                project_item.append(project_item)
        return project_item

    def save_project_item(self, project_item, project):
        if type(project_item) == type(dict()):
            for key, p_entry in project_item.iteritems():
                pi_i = ProjectItem()
                pi_i.project = project
                pi_i.name = key
                if type(p_entry) == type(dict()):
                    pi_i.value = type(p_entry)
                    pi_i.iterable = True
                    pi_i.save()
                    pe = Entry()
                    pe.save_entry(p_entry, pi_i)
                else:
                    pi_i.value = p_entry
                    pi_i.save()
            return ProjectItem.objects.values_list() 

        if type(project_item) == type(str()):
            pi_i = ProjectItem()
            pi_i.project = project
            pi_i.name = "<type 'str'>"
            pi_i.save()
        return pi_i
