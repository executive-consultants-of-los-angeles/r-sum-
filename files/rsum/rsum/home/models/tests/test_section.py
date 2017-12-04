# -*- coding: utf-8 -*-
"""Test cases for the Section model. """
from __future__ import unicode_literals

import yaml

from django.conf import settings

import home.models.profile as profile
import home.models.section as section


class TestSection(object):
    """Class for testing Section model saves.

    .. attribute:: profile

       The profile that contains the tested section.

    .. attribute:: section

       The section to be tested.
    """
    profile = profile.Profile()
    section = section.Section()
    abridged = {}

    def test_load_file(self):
        """Setup method for SectionTestCase class."""
        directory = settings.rsum.xander.values.get('dir')
        filename = settings.rsum.xander.values.get('name')

        yml_file = open((
            "/srv/rsum/cvs/{directory}/{filename}.yml"
        ).format(
            directory=directory, filename=filename))
        self.abridged = yaml.load(yml_file.read())
        yml_file.close()
        self.profile.name = 'abridged'
        self.profile.save()

    def test_section(self):
        """Test for saving Section model objects.

        :param: None
        """
        for item in sorted(
                self.abridged.items(),
                key=lambda t: t[1].get('id')
        ):
            stype = type(self.section)
            assert isinstance(item, stype)
