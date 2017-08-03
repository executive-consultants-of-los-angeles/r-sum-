#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from project import Project

import json


class SubSection(models.Model):
    section = models.ForeignKey('home.Section', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)

    def get_sub_section(self, section):
        # print(SubSection.objects.filter(section=section).values())
        subsections = []
        for subsection in list(
            SubSection.objects.filter(
                section=section
            ).order_by('id').values()
        ):
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
        projects = []
        if getattr(section, 'name') == 'experience':
            # print("\n\n\nsubsection\n\n\n")
            for k, v in sub_section.items():
                if k == 'introduction':
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
            # for k, v in sorted(
            #   subsection.items(),
            #   key = lambda t: t[1].get('id')
            # ):
            #    cv_d.items(),
            #    key = lambda t:t[1].get('id')
            # ):
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

        if isinstance(sub_section, list):
            for c, i in enumerate(sub_section):
                ss_i = SubSection()
                ss_i.section = section
                ss_i.content = type(sub_section)
                ss_i.name = str(c)
                ss_i.save()
                p = Project()
                projects.append(p.save_projects(i, ss_i, c))
            return projects

    class Meta:
        app_label = "home"
        managed = True
