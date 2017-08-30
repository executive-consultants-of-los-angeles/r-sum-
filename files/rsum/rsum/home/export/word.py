#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docx

from StringIO import StringIO

from docx import Document
from docx.shared import Cm 
from docx.shared import Pt 
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE

import home.schema

CV = home.schema.cv.CV


class ExportDocument(object):
    def __init__(self):
        self.name = 'alex-harris-cv.docx'

    def export(self, cv_id):
        cv_instance = CV()
        cv = cv_instance.get_cv(cv_id)
        stream = StringIO()
        document = Document()
        document = self.set_styles(document)
        document = self.set_layout(document)

        for current,section in enumerate(cv.get('sections')):
            #document.add_heading(section.get('name'))
            #self.add_section(section.get('content'), document)

            if section.get('name') == u'intro':
                self.add_intro(section.get('content'), document)

        document.save(stream)

        return stream 

    def add_section(self, section, document):
        for subsection in section:
            document.add_heading(subsection.get('name').replace('_',' '), level=2)
            if (
                isinstance(subsection.get('content'), list) and
                len(subsection.get('content')) > 0
            ):
                content = subsection.get('content')[0].get('content')
                print(type(content))
                document.add_paragraph(content)

    def add_intro(self, intro, document):
        for index, item in enumerate(sorted(intro)):
            item_content = item.get('content')[0].get('content')
            print(item_content)
            if (
                isinstance(item_content, unicode) or
                isinstance(item_content, str)
            ):
                document.add_heading(item_content, level=index+1)
        return None

    def set_styles(self, document):
        document.styles['Heading 1'].delete()
        document.styles.add_style('Heading 1', WD_STYLE_TYPE.PARAGRAPH, builtin=True) 
        style = document.styles['Heading 1'] 
        font = style.font
        font.color.rgb = RGBColor(0x51, 0x57, 0x6A) 
        font.name = 'Hind'
        font.size = Pt(24) 
        font.bold = True

        document.styles['Heading 2'].delete()
        document.styles.add_style('Heading 2', WD_STYLE_TYPE.PARAGRAPH, builtin=True)
        style = document.styles['Heading 2']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.size = Pt(16)

        return document

    def set_layout(self, document):
        sections = document.sections 
        section = sections[0] 
        section.page_height = Cm(29.7)
        section.page_width = Cm(21)
        section.left_margin = Cm(0.5)
        section.top_margin = Cm(0.5)
        section.right_margin = Cm(0.5)
        section.bottom_margin = Cm(0.5)

        return document
