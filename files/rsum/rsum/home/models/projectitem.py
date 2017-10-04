#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that definies ProjectItem objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from entry import Entry

import json


class ProjectItem(models.Model):
    """Class that definies ProjectItem objects.

    .. attribute:: project 

       Associated :obj:`home.models.project.Project` object.
    
    .. attribute:: name 

       Name for stored ProjectItem content.

    .. attribute:: content

       Stored ProjectItem content.
    """
    project = models.ForeignKey('home.Project', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.TextField(null=True)

    def get_project_item(self, project):
        """Get a ProjectItem object.

        :param project: Associated :obj:`home.models.project.Project` object.
        :type project: :obj:`home.models.project.Project`
        :return: A dictionary of ProjectItem values or a list of same.
        :rtype: dict(str, str) or list(dict) 
        """
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
            #: print(e)
            """
            .. todo:: Something with this Exception.
            """
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
        #: print(json.dumps(project_items, indent=1))
        return project_items

    def save_project_item(self, project_item, project):
        """Save a ProjectItem.

        :param project_item: The data that is to be saved to the ProjectItem
            model.
        :type project_item: dict(str, str) or str
        :param project: The associated :obj:`home.models.project.Project` object.
        :type project: :obj:`home.models.project.Project`
        :return: Dictionary containing the avlues saved to ProjectItem.
        :rtype: dict(str, str)
        """
        if isinstance(project_item, list):
            print('save the list you dolt!')

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

        if (
            isinstance(project_item, str) or
            isinstance(project_item, unicode)
        ):
            pi_i = ProjectItem()
            pi_i.project = project
            pi_i.content = project_item
            pi_i.name = project.name 
            pi_i.save()
        return ProjectItem.objects.values() 

    class Meta:
        app_label = 'home'
        managed = True
