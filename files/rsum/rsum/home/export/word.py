#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StringIO import StringIO

from docx import Document
from docx.shared import Inches

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

        for current,section in enumerate(cv.get('sections')):
            document.add_heading(section.get('name'))
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
        for item in intro:
            print(item.get('content'))
            document.add_heading(str(type(item)))
            if (
                isinstance(item.get('content'), unicode) or
                isinstance(item.get('content'), str)
            ):
                item_string = item.get('content')
                document.add_heading(item_string)
        return None
