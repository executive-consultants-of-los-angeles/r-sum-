#!/usr/bin/env python
# pylint: disable=no-member,redefined-builtin
# -*- coding: utf-8 -*-
"""Module for exporting profiles to Word format."""
import importlib
import json

from django.conf import settings as django_settings

from docx import Document

from export.tools import layout
from export.tools import style
from home.models.profile import Profile


def load_class(class_name):
    """Dynamically load a class.

    Special thanks to: `Thomas Sileo`_.

    .. _Thomas Sileo: http://bit.ly/2DsSINZ
    """
    class_data = class_name.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)


class ExportDocument(object):
    """Class to handle exporting rsum pages to Word documents.

    .. attribute:: document

       Document object for export.

    .. attribute:: settings

       Settings for the current app.
    """

    document = Document()
    settings = django_settings

    def __init__(self):
        """Initialize ExportDocument class.

        :return: None
        :rtype: None
        """
        settings = self.settings
        self.name = '{0}-profile.docx'.format(settings.DIR)

    def export_word(self, profile_id):
        """Export a word document.

        :param profile_id: ID of CV to export.
        :type profile_id: int
        :return: Stream of Word document for end user.
        :rtype: object
        """
        profile = Profile.objects.get(pk=profile_id)
        stream = StringIO()
        document = self.document
        document = style.set_styles(document)
        document = layout.set_layout(document)

        sections = json.loads(profile.content)

        for section in sections:
            document = self.save_section(section)

        document.save(self.name)

        return document

    def save_section(self, section):
        """Save a section of a document."""
        for name, value in section.items():
            section_cls = load_class('export.sections.{}.{}'.format(
                name, name.title()))
            section_obj = section_cls()
            self.document = section_obj.save(name, value, self.document)
        return self.document
