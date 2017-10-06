#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module containing the Profile Model class."""
import json
import yaml

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

from section import Section


class Profile(models.Model):
    """The Profile Model class.

    .. attribute:: name

       Name of the current Profile.

    .. attribute:: content
    
       JSON encoded content for the current profile.
    """
    name = models.CharField(max_length=200)
    content = JSONField()

    @classmethod
    def create(cls, *args, **kwargs):
        """Check to see if the current Profile Model already has sections.

        :param cls: The current class instance.
        :type cls: :obj:`home.models.profile.Profile`
        :return: ID of the current Profile object.
        :rtype: int
        """
        with open(settings.FILE, 'r') as yaml_file:
            raw_content = yaml.load(yaml_file.read())
        yaml_file.close()
        profile = cls(
            name=settings.OWNER,
            content=json.dumps(raw_content))
        profile.save()

        for item in raw_content:
            name = item.items()[0][0]
            section = item.items()[0][1]
            Section.create(name=name, content=section, profile=profile)

        return profile 
