#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model class that handles Section objects."""
import json

from django.db import models
from django.contrib.postgres.fields import JSONField


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
        content = kwargs.get('content')
        profile = kwargs.get('profile')
        section = cls(
            name=name,
            content=json.dumps(content),
            profile=profile)
        section.save()
        return section

    class Meta:
        app_label = 'home'
