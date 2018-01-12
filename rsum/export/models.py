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
        for section in sections:
            print(section.items())
            for name, local_section in section.items():
                if name == u'intro':
                    document = self.add_intro(local_section, document)

                if name == u'summary':
                    paragraph = document.add_paragraph('')
                    paragraph.paragraph_format.line_spacing = 0.0
                    document = self.add_summary(local_section, document)

                if name == u'skills':
                    paragraph = document.add_paragraph('')
                    paragraph.paragraph_format.line_spacing = 0.0
                    document = self.add_skills(local_section, document)

                if name == u'experience':
                    paragraph = document.add_paragraph('')
                    paragraph.paragraph_format.line_spacing = 0.0
                    paragraph.paragraph_format.page_break_before = True
                    document = self.add_experience(local_section, document)

                if name == u'education':
                    paragraph = document.add_paragraph('')
                    paragraph.paragraph_format.line_spacing = 0.0
                    document = self.add_education(local_section, document)

                if name == u'contact':
                    paragraph = document.add_paragraph('')
                    paragraph.paragraph_format.line_spacing = 0.0
                    document = self.add_contact(local_section, document)

        document.save(stream)

        return stream
    def add_skills(self, skills, document):
        """Add skills section.

        :param skills: Skills section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Skills.
        :rtype: object
        """
        current_year = datetime.datetime.now().strftime("%Y")

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
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
                t_sub.cell(index-1, 1).text = experience

                p = t_sub.cell(index-1, 1).paragraphs[0]
                p.style = 'Skill'
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                t_sub = self.add_sub_skills(skill, t_sub, index-1)
            index = index + 1
        return document

    def add_sub_skills(self, subs, ts, ts_index):
        """Add sub skills to skills section.

        :param subs: Sub skills to add to document.
        :type subs: [dict(str, str)]
        :param object ts: Table cell to update.
        :param int ts_index: Index for current table cell.
        :return: Document updated with sub skills.
        :rtype: object
        """
        current_year = float(datetime.datetime.now().strftime("%Y"))
        sub_table = ts.cell(ts_index, 0).add_table(rows=1, cols=2)
        index = 0
        for name, sub in subs.items():
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
                p = sub_table.cell(index, 0).paragraphs[0]
                p.style = 'Sub Skill'
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
                p = sub_table.cell(index, 1).paragraphs[0]
                p.style = 'Sub Skill'
                p.paragraph_format.line_spacing = 1.0
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                p.paragraph_format.space_after = 0
                index = index + 1
        return ts

    def add_experience(self, experience, document):
        """Add experience section.

        :param [dict(str, str)] experience:
            Experience section to add to document.
        :param object document: Document to update.
        :return: Document updated with Experience section.
        :rtype: object
        """
        s = self.s
        del experience[0]
        p = document.add_paragraph(
            'Experience',
            style='Heading 3')
        t = document.add_table(rows=1, cols=3)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for index, value in enumerate(experience):
            if index % 3 == 0:
                t.add_row()

            for name, item in value.items():
                row = (index % 9) / 3
                col = index % 3
                if (
                        index % 9 == 0 and
                        index > 0
                ):
                    t = document.add_table(rows=1, cols=3)
                    t.alignment = WD_TABLE_ALIGNMENT.CENTER

                if (
                        index % 18 == 0
                        and index > 17
                ):
                    document.add_page_break()
                    t = document.add_table(rows=1, cols=3)
                    t.alignment = WD_TABLE_ALIGNMENT.CENTER
                p = t.cell(row, col).paragraphs[0]
                p.paragraph_format.line_spacing = 0.0
                t.cell(row, col).add_picture(
                    '/srv/rsum/static/{}/img/970x647/{}.jpg'.format(
                        s.DIR,
                        index+1
                    ),
                    width=Cm(4.8)
                )
                p = t.cell(row, col).paragraphs[1]
                p.paragraph_format.space_after = 0

                p = t.cell(row, col).add_paragraph(
                    item.get('position'),
                    style='Heading 4')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
                p = t.cell(row, col).add_paragraph(
                    item.get('company'),
                    style='Heading 5')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = 0
                p = t.cell(row, col).add_paragraph(
                    "{0}, {1}".format(
                        item.get('location'),
                        item.get('duration')),
                    style='Heading 6')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = 0
                t = self.add_projects(item.get('projects'), t, row, col)
        p = document.add_paragraph('')
        p.paragraph_format.line_spacing = 0
        return document

    def add_projects(self, projects, table, row, col):
        """Add projects to experience section.

        :param [dict(str, str)] projects:
            Projects for a portion of Experience section.
        :param object table: Table from current document.
        :param int row: Index of current row.
        :param int col: Index of current col.
        :return: Updated Projects table.
        :rtype: object
        """
        for name, project in projects.items():
            p = table.cell(row, col).add_paragraph(
                name.replace('_', ' ').title(),
                style='List Bullet')
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = 0
            for item in project:
                p = table.cell(row, col).add_paragraph(
                    item,
                    style='List Bullet 2')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
        return table

    def add_education(self, education, document):
        """Add education section.

        :param [dict(str, str)] education:
            Education section for current document.
        :param object document: Current document.
        :return: Current document with Educaiton section.
        :rtype: object
        """
        s = self.s
        p = document.add_paragraph(
            'Education',
            style='Heading 3')
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_after = 0
        p.paragraph_format.page_break_before = True
        document.add_picture(
            '/srv/rsum/static/{0}/img/1920x1080/01.jpg'.format(
                s.DIR),
            width=Cm(4))
        p = document.add_paragraph(
            education.get('name'),
            style='Heading 4')
        p.paragraph_format.space_before = 0
        p = document.add_paragraph(
            education.get('studies'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = document.add_paragraph(
            "{0}, {1}".format(
                education.get('location'),
                education.get('duration')),
            style='Heading 6')
        p.paragraph_format.space_before = 0
        for name, project in education.get('projects').items():
            p = document.add_paragraph(
                name.title(),
                style='List Bullet')
            for item in project:
                p = document.add_paragraph(
                    item,
                    style='List Bullet 2')
        return document

    def add_contact(self, contact, document):
        """Add contact section.

        :param [dict(str, str)] contact:
            Contact section for current document.
        :param object document: Current document.
        :return: Current document with Contact section.
        :rtype: object
        """
        document.add_paragraph(contact.get('title'), style='Heading 3')
        p = document.add_paragraph(contact.get('message'), style='Normal')
        p.paragraph_format.space_after = 0
        t = document.add_table(rows=2, cols=6)
        p = t.cell(0, 0).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(0, 0).add_paragraph(
            'Website',
            style='Heading 4')
        p = t.cell(0, 0).add_paragraph(
            contact.get('web'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(0, 1).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(0, 1).add_paragraph(
            'Email',
            style='Heading 4')
        p = t.cell(0, 1).add_paragraph(
            contact.get('email'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(1, 0).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(1, 0).add_paragraph(
            'Phone',
            style='Heading 4')
        p = t.cell(1, 0).add_paragraph(
            contact.get('phone'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(1, 1).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(1, 1).add_paragraph('Location', style='Heading 4')
        p = t.cell(1, 1).add_paragraph(
            contact.get('location'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        return document

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
