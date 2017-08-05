#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section

import yaml


class SectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        cv = CV()
        cv.name = 'abridged'
        cv.template = 'acecv'
        cv.save()
        self.cv = cv

    def test_save_section(self):
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
    def setUp(self):
        cv_instance = CV()
        cv_id = cv_instance.check_sections(cvname='abridged', template='acecv')
        self.cv_id = cv_id
        section_instance = Section()
        self.sections = section_instance.get_sections(
            CV.objects.filter(id=cv_id)
        )

    def test_get_section(self):
        section_instance = Section()
        sections = section_instance.get_sections(
            CV.objects.filter(id=self.cv_id)
        )
        self.assertEqual(
            self.sections,
            sections
        )
