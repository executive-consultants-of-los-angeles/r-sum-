#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model class that handles Section objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from subsection import SubSection

import json


class Section(models.Model):
    """Class to define Section objects.

    .. attribute:: cv

       Related :obj:`home.models.cv.CV` object.

    .. attribute:: name

       Name of Section object for reference.

    .. attribute:: content

       Content for Section object.
    """
    cv = models.ForeignKey(
        'home.CV',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, default='section')
    content = models.TextField()

    def get_sections(self, cv):
        """Get all Section objects for a document.

        :param cv: Related :obj:`home.models.cv.CV` object.
        :type cv: :obj:`home.models.cv.CV`
        :return: List of dicionaries containing Section data.
        :rtype: list(dict(str, str)
        """
        sections = [] 
        for section in list(
            Section.objects.filter(
                cv=cv
            ).order_by('id').values()
        ):
            if section.get('content') == u"<type 'list'>":
                ss = SubSection(section=self)
                section.update({
                    'content': ss.get_sub_section(
                        Section.objects.filter(
                            id=section.get('id')
                        )
                    ),
                })
            if section.get('content') == u"<type 'dict'>":
                ss = SubSection(section=self)
                section.update({
                    'content': ss.get_sub_section(
                        Section.objects.filter(
                            id=section.get('id')
                        )
                    ),
                })
            sections.append(section)
        return sections

    def save_section(self, cv, section, name):
        """Save one Section object.
        
        :param cv: Related :obj:`home.models.cv.CV` object.
        :type cv: :obj:`home.models.cv.CV`
        :param section: Content for storage in the Section.
        :type section: dict(str, str) or str
        :param name: Name of current Section.
        :type name: str
        :return: Dictionary of values stored in Section.
        :rtype: dict(str, str)
        """
        if section is None:
            return None
        s_i = Section()
        s_i.cv = cv
        s_i.name = name

        if isinstance(section, str):
            s_i.content = section
            s_i.save()
        else:
            s_i.content = type(section)
            s_i.save()
            ss = SubSection()
            ss.save_sub_sections(section, s_i)

        return Section.objects.values()

    class Meta:
        app_label = "home"
        managed = True
