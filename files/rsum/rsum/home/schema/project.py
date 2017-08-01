#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from projectitem import ProjectItem

class Project(models.Model):
    sub_section = models.ForeignKey('home.SubSection', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)

    def get_projects(self, subsection):
        projects = []
        for project in list(
            Project.objects.filter(
                sub_section = subsection
            ).values()
        ):
            pli = ProjectItem()
            if project.get('value') == u"<type 'dict'>":
                project.update({
                    'value': pli.get_project_items(
                        Project.objects.filter(
                            id = project.get('id')
                        )
                    ) 
                })
                
            projects.append(project) 
        return projects

    def save_projects(self, projects, sub_section):
        if type(projects) == type(dict()):
            for k, v in projects.iteritems():
                p_i = Project()
                p_i.sub_section = sub_section
                p_i.name = k 
                if type(v) == type(dict()):
                    p_i.value = type(v)
                    p_i.save()
                    pi = ProjectItem()
                    pi.save_project_item(v, p_i)
                else:
                    p_i.value = v
                    p_i.save()
            return Project.objects.values_list() 

        if type(projects) == type(list()):
            for k,v in enumerate(projects):
                p_i = Project()
                p_i.sub_section = sub_section
                p_i.name = k
                p_i.value = type(v)
                p_i.save()
                pi = ProjectItem()
                pi.save_project_item(v, p_i)
            return Project.objects.values_list()

        if type(projects) == type(str()):
            p_i = Project()
            p_i.sub_section = sub_section
            p_i.value = projects
            p_i.save()


    class Meta:
        app_label = "home"
