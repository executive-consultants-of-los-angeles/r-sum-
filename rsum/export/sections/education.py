"""Module for education."""
# pylint: disable=no-name-in-module,no-member
from django.conf import settings as django_settings
from docx.shared import Cm


class Education(object):
    """Education export object."""

    name = None
    document = None
    settings = django_settings

    def save(self, section, document, graphics):
        """Short summary.

        Parameters
        ----------
        section : type
            Description of parameter `section`.
        document : type
            Description of parameter `document`.
        graphics : type
            Description of parameter `graphics`.

        Returns
        -------
        type
            Description of returned object.

        Raises
        -------
        ExceptionName
            Why the exception is raised.

        """
        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0
        settings = self.settings
        if graphics:
            document = self.get_education_graphics(name, section, document)
        else:
            document = self.get_education(name, section, document)
        return document

    def get_education(self, name, section, document):
        """Add education section.

        :param [dict(str, str)] education:
            Education section for current document.
        :param object document: Current document.
        :return: Current document with Educaiton section.
        :rtype: object
        """
        education = section
        paragraph = document.add_paragraph(
            'Education',
            style='Heading 3')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_after = 0
        paragraph.paragraph_format.page_break_before = True
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

    def get_education_graphics(self, name, section, document):
        """Add education section.
        :param [dict(str, str)] education:
            Education section for current document.
        :param object document: Current document.
        :return: Current document with Educaiton section.
        :rtype: object
        """
        education = section
        settings = self.settings
        paragraph = document.add_paragraph(
            'Education',
            style='Heading 3')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_after = 0
        paragraph.paragraph_format.page_break_before = True
        document = self.set_education_picture(settings, document)
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

    def set_education_picture(self, settings, document):
        """Sets the picture for display in the education section.

        Parameters
        ----------
        settings : type
            Description of parameter `settings`.
        document : type
            Description of parameter `document`.

        Returns
        -------
        :obj:docx.document
            Update document object.
        """
        document.add_picture(
            'static/profiles/{0}/img/1920x1080/01.jpg'.format(
                settings.DIR),
            width=Cm(4))
        return document
