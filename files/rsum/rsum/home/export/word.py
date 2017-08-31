#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docx

from StringIO import StringIO

from docx import Document
from docx.shared import Cm 
from docx.shared import Pt 
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

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

        for current,section in sorted(enumerate(cv.get('sections'))):
            if section.get('name') == u'intro':
                document = self.add_intro(section.get('content'), document)

            if section.get('name') == u'summary':
                document.add_paragraph('')
                document = self.add_summary(section.get('content'), document)

        document.save(stream)

        return stream 

    def add_intro(self, intro, document):
        table = document.add_table(rows=1, cols=2)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        print(table.alignment)
        for index, item in enumerate(sorted(intro)):
            if len(item.get('content')) == 1:
                content = item.get('content')[0].get('content')
                table.cell(0,0).add_paragraph(content, style='Heading '+str(index+1))
            else:
                # Need to add image linking support to docx.
                # print(item.get('content'))
                pass

        table.cell(0,0).width = Cm(12)
        table.cell(0,1).add_picture('/srv/rsum/static/acv/img/mockup/avatar-01.png', width=Cm(4))
        table.cell(0,1).width = Cm(4)
        table.cell(0,1).paragraphs[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return document 

    def add_summary(self, summary, document):
        t = document.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for index, item in enumerate(sorted(summary)):
            if len(item.get('content')) == 1:
                t.cell(0,0).add_picture('/srv/rsum/static/acv/img/500x700/01.jpg', width=Cm(5))
                t.cell(0,1).add_paragraph('Summary', style='Heading 1')
                t.cell(0,1).add_paragraph(item.get('content')[0].get('content'), style='Normal')
                t.cell(0,1).width = Cm(11)
                print(item)
        return document 

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

        document.styles['Normal'].delete()
        document.styles.add_style('Normal', WD_STYLE_TYPE.PARAGRAPH, builtin=True)
        style = document.styles['Normal']
        font = style.font
        font.name = 'Hind'
        font.color.rgb = RGBColor(0xA6, 0xA7, 0xAA)
        font.size = Pt(12)
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
