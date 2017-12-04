# -*- coding: utf-8 -*-
"""Test cases for the home.schema.cv module."""
from __future__ import unicode_literals

import yaml

from django.conf import settings

import home.models.profile as profile


class TestProfile(object):
    """TestProfile class.

    .. attribute:: abridged

       Dictionary containing an abridged profile.

    .. attribute:: profile

       Profile for testing with.
    """
    abridged = {}
    profile = profile.Profile()

    def test_load_from_file(self):
        """Set up the CVTestCase class."""
        yml_file = open(("/srv/rsum/cvs/{directory}/{filename}.yml").format(
            directory=settings.DIR, filename=settings.NAME), 'r')
        self.abridged = yaml.load(yml_file.read())
        yml_file.close()

    def test_create_profile(self):
        """This tests creating a profile."""

        profile_result = self.profile.create()
        assert isinstance(profile_result, type(self.profile))
