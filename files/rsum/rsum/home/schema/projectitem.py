#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from entry import Entry

import json


class ProjectItem(models.Model):
    project = models.ForeignKey('home.Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField(null=True)
    iterable = models.BooleanField(default=False)

    def get_project_item(self, project):
        try:
            name = list(project.values())[0].get('name')
            pid = {
                name: {}
            }

            for pi in list(
                ProjectItem.objects.filter(
                    project=project
                ).order_by('id').values()
            ):
                pid.get(name).update({
                    pi.get('name'): pi.get('content')
                })
            return pid
        except Exception as e:
            print(e)
            pass

        project_items = []
        for project_item in list(
            ProjectItem.objects.filter(
                project=project
            ).order_by('id').values()
        ):
            if project_item.get('content') == u"<type 'dict'>":
                pe = Entry()
                project_item.update({
                    'content': pe.get_entry(
                        ProjectItem.objects.filter(
                            id=project_item.get('id')
                        )
                    )
                })
                project_items.append(project_item)
            else:
                project_items.append({
                    project_item.get('name'): project_item.get('content')
                })
        # print(json.dumps(project_items, indent=1))
        return project_items

    def save_project_item(self, project_item, project):
        if isinstance(project_item, dict):
            for key, p_entry in project_item.iteritems():
                pi_i = ProjectItem()
                pi_i.project = project
                pi_i.name = key
                if isinstance(p_entry, dict):
                    pi_i.content = type(p_entry)
                    pi_i.iterable = True
                    pi_i.save()
                    pe = Entry()
                    pe.save_entry(p_entry, pi_i)
                else:
                    pi_i.content = p_entry
                    pi_i.save()
            return ProjectItem.objects.values()

        if isinstance(project_item, str):
            pi_i = ProjectItem()
            pi_i.project = project
            pi_i.name = "<type 'str'>"
            pi_i.save()
        return ProjectItem.objects.values() 

    class Meta:
        app_label = 'home'
        managed = True
