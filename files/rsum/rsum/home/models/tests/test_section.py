# -*- coding: utf-8 -*-
"""Test cases for the Section model. """
from __future__ import unicode_literals

import yaml

from django.test import TestCase
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

    def setUp(self):
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
        for section in sorted(
                self.abridged.items(),
                key=lambda t: t[1].get('id')
        ):
            stype = type(self.section)
            assert isinstance(section, stype)


class GetSectionTestCase(TestCase):
    """Class for testing Section model gets."""
    def setUp(self):
        """Setup for Section model get tests."""
        cv_instance = CV()
        cv_id = cv_instance.check_sections(name_of_owner='alex', name_of_cv='abridged', template='acecv')
        self.cv_id = cv_id
        section_instance = Section()
        self.sections = section_instance.get_sections(
            CV.objects.filter(id=cv_id)
        )

    def test_get_section(self):
        """Test Section moodel gets."""
        section_instance = Section()
        sections = section_instance.get_sections(
            CV.objects.filter(id=self.cv_id)
        )
        self.assertEqual(
            self.sections,
            sections
        )
