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
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH

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

    def add_intro(self, sections, document):
        """Add introduction section.

        :param intro: Introduction to add to document.
        :type intro: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Introduction.
        :rtype: object
        """
        intro = sections[0]
        settings = self.settings
        table = document.add_table(rows=1, cols=2)
        table.cell(0, 0).width = Cm(12)

        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.cell(0, 0).add_paragraph(
            intro.get('name'),
            style='Heading 1'
        )
        table.cell(0, 0).add_paragraph(
            intro.get('position'),
            style='Heading 2')

        table.cell(0, 1).width = Cm(4)
        table.cell(0, 1).add_picture(
            '/srv/rsum/static/{0}/img/mockup/avatar-02.png'.format(
                settings.DIR))
        table.cell(
            0,
            1
        ).paragraphs[
            0
        ].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return document

    def add_summary(self, sections, document):
        """Add summary section.

        :param summary: Summary section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Summary.
        :rtype: object
        """
        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0

        settings = self.settings
        summary = sections[1]
        summary_table = document.add_table(rows=1, cols=2)
        summary_table.alignment = WD_TABLE_ALIGNMENT.CENTER

        summary_table.cell(0, 0).width = Cm(6)
        summary_table.cell(0, 0).add_picture(
            '/srv/rsum/static/{0}/img/500x700/02.png'.format(settings.DIR),
            width=Cm(5))

        summary_table.cell(0, 1).add_paragraph('Summary', style='Heading 3')
        summary_table.cell(0, 1).add_paragraph(
            summary.get('content'), style='Normal')
        paragraph = summary_table.cell(0, 1).paragraphs[1]
        paragraph.paragraph_format.line_spacing = 1.0
        summary_table.cell(0, 1).width = Cm(10)
        paragraph = summary_table.cell(0, 0).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0.0
        paragraph = summary_table.cell(0, 1).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0.0
        return document

    def add_skills(self, sections, document):
        """Add skills section.

        :param skills: Skills section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Skills.
        :rtype: object
        """
        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0
        current_year = datetime.datetime.now().strftime("%Y")
        print(sections[2])
        skills = sections[2].get('skills')

        t = document.tables[1]
        t.cell(0, 1).add_paragraph('Skills', style='Heading 3')
        t_sub = t.cell(0, 1).add_table(rows=1, cols=2)
        t.cell(0, 1).tables[0].columns[0].width = Cm(7)
        index = 1
        for name, skill in skills.items():
            if isinstance(skill, dict):
                experience = int(current_year) - int(skill.get('start'))
                experience = '{0} year(s)'.format(str(experience))
                name = skill.get('name').replace('_', ' ').title()

                # Add a row to the sub table.
                t_sub.add_row()
                t_sub.cell(index-1, 0).text = name
                p = t_sub.cell(index-1, 0).paragraphs[0]
                p.style = 'Skill'
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.paragraph_format.space_after = 0
                t_sub.cell(index-1, 1).text = experience

                p = t_sub.cell(index-1, 1).paragraphs[0]
                p.style = 'Skill'
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.paragraph_format.space_after = 0
                paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                t_sub = self.add_sub_skills(skill, t_sub, index-1)
            index = index + 1
        return document

    @staticmethod
    def add_sub_skills(subs, skilltable, skilltable_index):
        """Add sub skills to skills section.

        :param subs: Sub skills to add to document.
        :type subs: [dict(str, str)]
        :param object ts: Table cell to update.
        :param int ts_index: Index for current table cell.
        :return: Document updated with sub skills.
        :rtype: object
        """
        current_year = float(datetime.datetime.now().strftime("%Y"))
        sub_table = skilltable.cell(
            skilltable_index, 0).add_table(rows=1, cols=2)
        index = 0
        for sub in subs:
            if isinstance(sub, dict):
                experience = int(current_year) - int(sub.get('start'))
                experience = '{0} year(s)'.format(str(experience))
                if index == 0:
                    sub_table.cell(0, 0).text = sub.get('name')
                    sub_table.cell(0, 1).text = experience
                    sub_table.cell(0, 0).width = Cm(5)
                else:
                    sub_table.add_row()
                    sub_table.cell(index, 0).text = sub.get('name')
                    sub_table.cell(index, 0).width = Cm(1)
                    sub_table.cell(index, 1).text = experience
                paragraph = sub_table.cell(index, 0).paragraphs[0]
                paragraph.style = 'Sub Skill'
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.paragraph_format.space_after = 0
                paragraph = sub_table.cell(index, 1).paragraphs[0]
                paragraph.style = 'Sub Skill'
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                paragraph.paragraph_format.space_after = 0
                index = index + 1
        return skilltable

    def add_education(self, sections, document):
        """Add education section.

        :param [dict(str, str)] education:
            Education section for current document.
        :param object document: Current document.
        :return: Current document with Educaiton section.
        :rtype: object
        """
        education = sections[5]
        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0
        settings = self.settings
        paragraph = document.add_paragraph(
            'Education',
            style='Heading 3')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_after = 0
        paragraph.paragraph_format.page_break_before = True
        document.add_picture(
            '/srv/rsum/static/{0}/img/1920x1080/01.jpg'.format(
                settings.DIR),
            width=Cm(4))
        paragraph = document.add_paragraph(
            education.get('name'),
            style='Heading 4')
        paragraph.paragraph_format.space_before = 0
        paragraph = document.add_paragraph(
            education.get('studies'),
            style='Heading 5')
        paragraph.paragraph_format.space_before = 0
        paragraph = document.add_paragraph(
            "{0}, {1}".format(
                education.get('location'),
                education.get('duration')),
            style='Heading 6')
        paragraph.paragraph_format.space_before = 0
        return document
