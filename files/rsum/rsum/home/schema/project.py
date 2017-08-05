#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from projectitem import ProjectItem

import json


class Project(models.Model):
    sub_section = models.ForeignKey(
        'home.SubSection',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)

    def get_projects(self, subsection):
        # print(subsection)
        projects = []
        for project in list(
            Project.objects.filter(
                sub_section=subsection
            ).values()
        ):
            pli = ProjectItem()
            if project.get('content') == u"<type 'dict'>":
                project.update({
                    'content': pli.get_project_item(
                        Project.objects.filter(
                            id=project.get('id')
                        )
                    )
                })

            projects.append(project)
            # print(json.dumps(projects,indent=1))
        return projects

    def save_projects(self, projects, sub_section, name):
        # print(json.dumps(projects, indent=1))
        # print(name)
        if name == 'id':
            return None

        if isinstance(projects, dict):
            for k, v in projects.iteritems():
                p_i = Project()
                p_i.sub_section = sub_section
                p_i.name = k
                if isinstance(v, dict):
                    p_i.content = type(v)
                    p_i.save()
                    pi = ProjectItem()
                    pi.save_project_item(v, p_i)
                else:
                    p_i.content = v
                    p_i.save()
            return Project.objects.values()

        if isinstance(projects, list):
            for k, v in enumerate(projects):
                p_i = Project()
                p_i.sub_section = sub_section
                p_i.name = name
                p_i.content = type(v)
                p_i.save()
                pi = ProjectItem()
                pi.save_project_item(v, p_i)
            return Project.objects.values()

        if (
            isinstance(projects, str) or
            isinstance(projects, unicode)
        ):
            p_i = Project()
            p_i.sub_section = sub_section
            p_i.name = name
            p_i.content = projects
            p_i.save()
            return Project.objects.values()

    class Meta:
        app_label = "home"
        managed = True
