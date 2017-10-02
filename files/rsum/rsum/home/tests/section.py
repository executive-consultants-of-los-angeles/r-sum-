#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test cases for the Section model. """
from __future__ import unicode_literals

import socket
import yaml

from django.test import TestCase

from home.schema.cv import CV
from home.schema.section import Section
from rsum.settings.rsum import values


class SectionTestCase(TestCase):
    """Class for testing Section model saves."""
    def setUp(self):
        """Setup method for SectionTestCase class."""
        s = values.get(socket.gethostname())
        f = open('/srv/rsum/cvs/{0}/{1}.yml'.format(s.get('dir'), s.get('name')))
        self.abridged = yaml.load(f.read())
        f.close()
        cv = CV()
        cv.name = 'abridged'
        cv.template = 'acecv'
        cv.save()
        self.cv = cv

    def test_save_section(self):
        """Test for saving Section model objects."""
        cv = self.cv

        for name, section in sorted(
            self.abridged.items(),
            key=lambda t: t[1].get('id')
        ):
            section_instance = Section()
            section_result = section_instance.save_section(
                cv,
                section,
                name
            )
            self.assertEqual(
                list(Section.objects.values()),
                list(section_result)
            )


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
