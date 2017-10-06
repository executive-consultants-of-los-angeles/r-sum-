#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for class that defines SubSection objects."""
import json

from django.db import models
from django.contrib.postgres.fields import JSONField

from sub_item import SubItem 


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
        sub_section = cls(
            name=name,
            content=json.dumps(content),
            section=section)
        sub_section.save()

        if isinstance(content, list):
            [SubItem.create(
                name=name,
                content=sub_item,
                sub_section=sub_section
            ) for name, sub_item in enumerate(content)]
            return sub_section

        if isinstance(content, dict):
            for name, sub_item in content.items():
                SubItem.create(
                    name=name,
                    content=sub_item,
                    sub_section=sub_section)
        return sub_section
