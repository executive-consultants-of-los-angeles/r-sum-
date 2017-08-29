#!/usr/bin/env python
# -*- coding: utf-8 -*-

from StringIO import StringIO

from docx import Document
from docx.shared import Inches

import home.schema

CV = home.schema.cv.CV
print(CV)


class ExportDocument(object):
    def __init__(self):
        self.name = 'alex-harris-cv.docx'

    def export(self, cv_id):
        cv_instance = CV()
        cv = cv_instance.get_cv(cv_id)
        stream = StringIO()
        document = Document()

        for section in cv.get('sections'):
            print(section.get('name'))
            document.add_heading(section.get('name'))
            document.add_section(self.get_section(section))

        document.save(stream)

        return stream 

    def get_section(self, section):
        print(section) 
