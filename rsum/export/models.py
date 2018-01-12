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

    def set_styles(self, document):
        """Set styles in the Word document.

        :param object document: Current document.
        :return: Current document with correct styles.
        :rtype: object
        """
        style = document.styles['Heading 1']
        font = style.font
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.name = 'Hind'
        font.size = Pt(24)
        font.bold = True

        style = document.styles['Heading 2']
        font = style.font
        font.name = 'Hind'
        font.italic = False
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.size = Pt(16)

        style = document.styles['Heading 3']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.size = Pt(14)
        font.bold = True

        style = document.styles['Heading 4']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.size = Pt(8)
        font.bold = True
        font.italic = False

        style = document.styles['Heading 5']
        font = style.font
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.small_caps = True
        font.name = 'Hind'
        font.size = Pt(7)

        style = document.styles['Heading 6']
        font = style.font
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.name = 'Hind'
        font.size = Pt(6)
        font.bold = True
        font.italic = False

        style = document.styles['List Bullet']
        font = style.font
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.name = 'Hind'
        font.size = Pt(5)
        font.bold = True

        style = document.styles['List Bullet 2']
        font = style.font
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.size = Pt(5)
        font.name = 'Hind'

        document.styles.add_style('Skill', WD_STYLE_TYPE.PARAGRAPH)
        style = document.styles['Skill']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.size = Pt(9)
        font.bold = True

        document.styles.add_style('Sub Skill', WD_STYLE_TYPE.PARAGRAPH)
        style = document.styles['Sub Skill']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A)
        font.size = Pt(7)

        style = document.styles['Normal']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.size = Pt(11)
        return document

    def set_layout(self, document):
        """Define document layout.

        :param object document: Current document.
        :return: Current document with adjusted layout.
        :rtype: object
        """
        sections = document.sections
        section = sections[0]
        section.page_height = Cm(29.7)
        section.page_width = Cm(21)
        section.left_margin = Cm(0.5)
        section.top_margin = Cm(0.5)
        section.right_margin = Cm(0.5)
        section.bottom_margin = Cm(0.5)

        return document
