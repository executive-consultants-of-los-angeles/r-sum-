#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module containing the Profile Model class."""
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import json
import socket
import yaml

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

from section import Section
from sub_section import SubSection


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

        return None
