#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for class that defines SubSection objects."""
from django.db import models
from django.contrib.postgres.fields import JSONField

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
    content = JSONField()

    @classmethod
    def create(cls, name='default', *args, **kwargs):
        """Class method to handle creation of SubSection objects for testing.
        
        :param cls: The SubSection class.
        :type cls: :obj:`home.models.subsection.SubSection`
        :param str name: Name of the sub section.
        :param str content: Content for the sub section.
        :return: Reference to the created SubSection.
        :rtype: :obj:`home.models.subsection.SubSection`
        """
        content = kwargs.get('content')
        section = kwargs.get('section')
        sub_section = cls(name=name, content=content, section=section)
        sub_section.save()
        return sub_section 
