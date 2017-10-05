#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model class that handles Section objects."""
import json

from collections import OrderedDict

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

from sub_section import SubSection


class Section(models.Model):
    """Class to define Section objects.

    .. attribute:: profile

       Related :obj:`home.models.profile.Profile` object.

    .. attribute:: name

       Name of Section object for reference.

    .. attribute:: content

       JSON encoded content for the current section. 
    """
    profile = models.ForeignKey(
        'home.Profile', 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, default='section')
    content = JSONField()

    @classmethod
    def create(cls, name='default', *args, **kwargs):
        """Class method to handle creation of Section objects for testing.
        
        :param cls: The Section class.
        :type cls: :obj:`home.models.section.Section`
        :param str name: Name of the section.
        :param str content: Content for the section.
        :return: Reference to the created Section.
        :rtype: :obj:`home.models.section.Section`
        """
        subsections = None 
        content = kwargs.get('content')
        profile = kwargs.get('profile')
        section = cls(name=name, content=content, profile=profile)
        section.save()

        for name, subsection in content.items():
            SubSection.create(name=name, content=subsection, section=section)

        return None
