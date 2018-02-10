"""Intro module."""
# pylint: disable=too-few-public-methods,no-name-in-module,no-member
from django.conf import settings as django_settings
from docx.enum.text import WD_ALIGN_PARAGRAPH


class Intro(object):
    """Class for Intro objects."""

    name = None
    document = None
    settings = django_settings

    def save(self, name, section, document):
        """Add introduction section.

        :param intro: Introduction to add to document.
        :type intro: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Introduction.
        :rtype: object
        """
        intro = section
        self.name = name
        paragraph = document.add_paragraph(
            intro.get('name'), style='Heading 1')

        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

        paragraph = document.add_paragraph(
            intro.get('position'), style='Heading 2')

        return document
