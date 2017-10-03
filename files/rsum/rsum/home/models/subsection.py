#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for class that defines SubSection objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from project import Project

import json


class SubSection(models.Model):
    """Class to define SubSection objects."""
    section = models.ForeignKey(
        'home.Section', 
        on_delete=models.CASCADE,
        related_name='section'
    )
    name = models.CharField(max_length=200)
    content = models.TextField()

    def get_sub_section(self, section):
        """Get a SubSection object."""
        # print(SubSection.objects.filter(section=section).values())
        subsections = []
        for subsection in list(
            SubSection.objects.filter(
                section=section
            ).order_by('id').values()
        ):
            if subsection.get('name') == 'build_status':
                subsection.update({'name': 'Build Status'})                

            # print(json.dumps(subsection, indent=1))
            p = Project()
            if (
                subsection.get('content') == u"<type 'list'>" or
                subsection.get('content') == u"<type 'dict'>"
            ):
                subsection.update({
                    'content': p.get_projects(
                        SubSection.objects.filter(
                            id=subsection.get('id')
                        )
                    )
                })
            else:
                subsection.update({
                    'content': list(
                        Project.objects.filter(
                            sub_section=subsection.get('id')
                        ).values()
                    )
                })
            subsections.append(subsection)
        return subsections

    def save_sub_sections(self, sub_section, section):
        """Save SubSection objects."""
        projects = []
        if (
            getattr(section, 'name') == 'experience' or
            getattr(section, 'name') == 'skills'
        ):
            # print("\n\n\nsubsection\n\n\n")
            for k, v in sub_section.items():
                if (
                    k == 'introduction' or
                    k == 'start'
                ):
                    ss_i = SubSection()
                    ss_i.section = section
                    ss_i.content = v
                    ss_i.name = k
                    ss_i.save()
                    del sub_section[k]
                elif k == 'id':
                    del sub_section[k]
        
            for item in sorted(
                sub_section.items(),
                key=lambda t: t[1].get('id')
            ):
                ss_i = SubSection()
                ss_i.section = section
                ss_i.content = type(item[1])
                ss_i.name = item[0]
                ss_i.save()
                p = Project()
                projects.append(p.save_projects(item[1], ss_i, item[0]))
                # print(json.dumps(item, indent=1))
                # print(type(item[1]))
            return projects

        if isinstance(sub_section, dict):
            for k, v in sub_section.iteritems():
                ss_i = SubSection()
                ss_i.section = section
                ss_i.content = type(sub_section)
                ss_i.name = k
                if k != 'id':
                    ss_i.save()
                    p = Project()
                    projects.append(p.save_projects(v, ss_i, k))
            return projects

    class Meta:
        app_label = "home"
        managed = True
