#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for exporting profiles to Word format."""
from __future__ import print_function

import datetime
import json
from io import StringIO

from django.conf import settings as django_settings

from docx import Document
from docx.shared import Cm
from docx.shared import Pt
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from home.models.profile import Profile


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
        self.name = '{0}-profile.docx'.format(settings.OWNER)

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
        document = self.set_styles(document)
        document = self.set_layout(document)
        paragraph = []

        sections = json.loads(profile.content)

        document.save(sections)

        return stream
