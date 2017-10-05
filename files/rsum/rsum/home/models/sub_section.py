#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for class that defines SubSection objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from sub_section_item import SubItem 

import json


class SubSection(models.Model):
    """Class to define SubSection objects.

    .. attribute:: section

       Related :obj:`home.models.section.Section` object.

    .. attribute:: name

       Name of SubSection.

    .. attribute:: content

       Content for SubSection.
    """
    section = models.ForeignKey(
        'home.Section', 
        on_delete=models.CASCADE,
        related_name='section'
    )
    name = models.CharField(max_length=200)
    content = models.TextField()

    @classmethod
    def create(cls, name='default', content='default'):
        """Class method to handle creation of SubSection objects for testing.
        
        :param cls: The SubSection class.
        :type cls: :obj:`home.models.subsection.SubSection`
        :param str name: Name of the sub section.
        :param str content: Content for the sub section.
        :return: Reference to the created SubSection.
        :rtype: :obj:`home.models.subsection.SubSection`
        """
        section = Section.create(name='default', content='default')
        sub_section = cls(name=name, content=content, section=section)
        sub_section.save()
        return sub_section 

    def get_sub_section(self, section):
        """Get a SubSection object.

        :param section:
            Related :obj:`home.models.section.Section` object.
        :type section: :obj:`home.models.section.Section`
        :return: List of dictionaries of retrieved SubSection values.
        :rtype: list(dict(str, str)
        """
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
            p = SubItem()
            if (
                subsection.get('content') == u"<type 'list'>" or
                subsection.get('content') == u"<type 'dict'>"
            ):
                subsection.update({
                    'content': p.get_sub_section_items(
                        SubSection.objects.filter(
                            id=subsection.get('id')
                        )
                    )
                })
            else:
                subsection.update({
                    'content': list(
                        SubItem.objects.filter(
                            sub_section=subsection.get('id')
                        ).values()
                    )
                })
            subsections.append(subsection)
        return subsections

    def save_sub_sections(self, sub_section, section):
        """Save SubSection objects.

        :param sub_section: Content to be stored in the SubSection model.
        :type sub_section: dict(str, str) 
        :param section: Related :obj:'home.models.section.Section` object.
        :type section: :obj:`home.models.section.Section`
        :return: Sorted or unsorted values saved in SubSection.
        :rtype: dict(str, str) or tuple(str, dict(str, str))
        """
        sub_section_items = []
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
                p = SubItem()
                sub_section_items.append(p.save_sub_section_items(item[1], ss_i, item[0]))
                # print(json.dumps(item, indent=1))
                # print(type(item[1]))
            return sub_section_items

        if isinstance(sub_section, dict):
            for k, v in sub_section.iteritems():
                ss_i = SubSection()
                ss_i.section = section
                ss_i.content = type(sub_section)
                ss_i.name = k
                if k != 'id':
                    ss_i.save()
                    p = SubItem()
                    sub_section_items.append(p.save_sub_section_items(v, ss_i, k))
            return sub_section_items

    class Meta:
        app_label = "home"
        managed = True
