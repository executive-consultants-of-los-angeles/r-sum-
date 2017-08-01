#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from project import Project

class SubSection(models.Model):
    section = models.ForeignKey('home.Section', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)

    def get_sub_section(self, section):
        subsections = []
        for subsection in list(
            SubSection.objects.filter(
                section = section
            ).order_by('id').values() 
        ):
            p = Project() 
            if (
                subsection.get('value') == u"<type 'list'>" or
                subsection.get('value') == u"<type 'dict'>"
            ):
                subsection.update({
                    'content': p.get_projects(
                        SubSection.objects.filter(
                            id = subsection.get('id')
                        )
                    )
                })
            else:
                subsection.update({
                    'content': list(
                        Project.objects.filter(
                            sub_section = subsection.get('id')  
                        ).values()
                    )
                })
            subsections.append(subsection)
        return subsections
                    
    
    def save_sub_sections(self, sub_section, section):
        projects = []
        if type(sub_section) == type(dict()):
            #for k, v in sorted(
            #    cv_d.items(), 
            #    key = lambda t:t[1].get('id')
            #):
            for k, v in sub_section.iteritems():
                ss_i = SubSection()
                ss_i.section = section
                ss_i.value = type(sub_section)
                ss_i.name = k
                ss_i.save()
                p = Project() 
                projects.append(p.save_projects(v, ss_i))
            return projects

        if type(sub_section) == type(list()):
            for c,i in enumerate(sub_section):
                ss_i = SubSection()
                ss_i.section = section
                ss_i.value = type(sub_section)
                ss_i.name = str(c) 
                ss_i.save()
                p = Project()
                projects.append(p.save_projects(i, ss_i))
            return projects 

    class Meta:
        app_label = "home"
        managed = True
