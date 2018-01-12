#!/usr/bin/env python
# pylint: disable=R0903
# -*- coding: utf-8 -*-
"""Module containing the Profile Model class."""
import json
import yaml

from django.db import models
from django.contrib.postgres.fields import JSONField
from .section import Section

OWNER = 'xander'


class Profile(models.Model):
    """The Profile Model class.

    .. attribute:: name

       Name of the current Profile.

    .. attribute:: content

       JSON encoded content for the current profile.
    """

    name = models.CharField(max_length=200, unique=True)
    content = JSONField(default={})

    @classmethod
    def create(cls):
        """Check to see if the current Profile Model already has sections.

        :param cls: The current class instance.
        :type cls: :obj:`home.models.profile.Profile`
        :return: The created instance of :obj:`home.models.profile.Profile`.
        :rtype: :obj:`home.models.profile.Profile`
        """
        with open(
            '/srv/static/profiles/xander/complete.yml', 'r'
        ) as yaml_file:
            raw_content = yaml.safe_load(yaml_file.read())
        yaml_file.close()
        profile = cls(
            name=OWNER,
            content=json.dumps(raw_content))
        profile.save()

        for item in raw_content:
            for entry, content in item.items():
                name = entry
                section = content
                Section.create(name=name, content=section, profile=profile)

        return profile

    class Meta:
        """Meta data."""

        app_label = 'home'
