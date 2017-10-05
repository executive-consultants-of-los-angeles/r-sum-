#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model class that handles Section objects."""
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from sub_section import SubSection

import json


class Section(models.Model):
    """Class to define Section objects.

    .. attribute:: profile

       Related :obj:`home.models.profile.Profile` object.

    .. attribute:: name

       Name of Section object for reference.

    .. attribute:: content

       Content for Section object.
    """
    profile = models.ForeignKey(
        'home.Profile',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, default='section')
    content = models.TextField()

    @classmethod
    def create(cls, name='default', content='default'):
        """Class method to handle creation of Section objects for testing.
        
        :param cls: The Section class.
        :type cls: :obj:`home.models.section.Section`
        :param str name: Name of the section.
        :param str content: Content for the section.
        :return: Reference to the created Section.
        :rtype: :obj:`home.models.section.Section`
        """
        profile = Profile.create(name='default')
        section = cls(name=name, content=content, profile=profile)
        section.save()
        return section 

    def get_sections(self, profile):
        """Get all Section objects for a document.

        :param profile: Related :obj:`home.models.profile.Profile` object.
        :type profile: :obj:`home.models.profile.Profile`
        :return: List of dicionaries containing Section data.
        :rtype: list(dict(str, str)
        """
        sections = [] 
        for section in list(
            Section.objects.filter(
                profile=profile
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

    def save_section(self, profile, section, name):
        """Save one Section object.
        
        :param profile: Related :obj:`home.models.profile.Profile` object.
        :type profile: :obj:`home.models.profile.Profile`
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
        s_i.profile = profile
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
