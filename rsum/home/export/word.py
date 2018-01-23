#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for exporting profiles to Word format."""
from __future__ import print_function

import json
from io import StringIO

from django.conf import settings as django_settings

from docx import Document
from docx.shared import Cm
from docx.enum.table import WD_TABLE_ALIGNMENT

from home.models.profile import Profile

from .experience import add_experience
from .contact import add_contact
from . import layout
from . import style


class ExportDocument(object):
    """Class to handle exporting rsum pages to Word documents.

    .. attribute:: s

       Hostname of current host.

    .. attribute:: name

       Filename to offer to the end user.
    """

    settings = django_settings

    def __init__(self):
        """Initialize ExportDocument class.

        :return: None
        :rtype: None
        """
        settings = self.settings
        self.name = '{0}-profile.docx'.format(settings.DIR)

    def export(self, profile_id):
        """Export a word document.

        :param profile_id: ID of CV to export.
        :type profile_id: int
        :return: Stream of Word document for end user.
        :rtype: object
        """
        profile = Profile.objects.get(pk=profile_id)
        stream = StringIO()
        document = Document()
        document = style.set_styles(document)
        document = layout.set_layout(document)

        sections = json.loads(profile.content)

        document = self.add_intro(sections, document)
        document = self.add_summary(sections, document)
        document = self.add_skills(sections, document)
        document = add_experience(self.settings, sections, document)
        document = self.add_education(sections, document)
        document = add_contact(sections, document)

        document.save(stream)

        return stream
