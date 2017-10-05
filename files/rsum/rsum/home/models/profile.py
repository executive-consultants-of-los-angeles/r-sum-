#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module containing the Profile Model class."""
import datetime
import json
import socket
import yaml

from collections import OrderedDict

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
        profile = cls(name=settings.OWNER, content=json.dumps(raw_content))
        profile.save()

        sections = OrderedDict(
            sorted(raw_content.items(), key=lambda k: k[1].get('id'))
        )

        for name, section in sections.items():
            Section.create(name=name, content=section, profile=profile)

        return profile 
