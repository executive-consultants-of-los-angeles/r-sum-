"""Styles module."""
# pylint: disable=no-member
from docx.shared import Pt
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.enum.text import WD_TAB_LEADER
from docx.shared import Cm


def set_first_headings(document):
    """Set top three headings on document.

    :param document: The document being manipulated.
    :returns: Document with new styles added.
    """
    style = document.styles['Heading 1']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(24)
    font.bold = True

    style = document.styles['Heading 2']
    font = style.font
    font.name = 'Calibri'
    font.italic = False
    font.size = Pt(16)

    style = document.styles['Heading 3']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(14)
    font.bold = True
    return document


def set_second_headings(document):
    """Set the second three headings.

    :param document: The document being manipulated.
    :returns: Document with new styles added.
    """
    style = document.styles['Heading 4']
    font = style.font
    font.size = Pt(8)
    font.bold = True
    font.italic = False

    style = document.styles['Heading 5']
    font = style.font
    font.small_caps = True
    font.name = 'Calibri'
    font.size = Pt(7)

    style = document.styles['Heading 6']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(6)
    font.bold = True
    font.italic = False
    return document


def set_list_bullets(document):
    """Set list bullet styles.

    :param document: The document being manipulated.
    :returns: Document with new styles added.
    """
    style = document.styles['List Bullet']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(5)
    font.bold = True

    style = document.styles['List Bullet 2']
    font = style.font
    font.size = Pt(5)
    font.name = 'Calibri'
    style.paragraph_format.tab_stops.add_tab_stop(
        Cm(0.1),
        alignment=WD_TAB_ALIGNMENT.LEFT,
        leader=WD_TAB_LEADER.SPACES
    )
    return document


def set_skill_styles(document):
    """Define remaining styles.

    :param document: The document being manipulated.
    :returns: Document with new styles added.
    """
    try:
        document.styles.add_style('Skill', WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        pass
    style = document.styles['Skill']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(9)
    font.bold = True

    try:
        document.styles.add_style('Sub Skill', WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        pass
    style = document.styles['Sub Skill']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(7)
    return document


def set_normal_style(document):
    """Define the normal style for the template.

    :param document: The document being manipulated.
    :returns: Document with new styles added.
    """
    style = document.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    return document


def set_styles(document):
    """Set styles in the Word document.

    :param object document: Current document.
    :return: Current document with correct styles.
    :rtype: object
    """
    document = set_first_headings(document)
    document = set_second_headings(document)
    document = set_list_bullets(document)
    document = set_skill_styles(document)
    document = set_normal_style(document)
    return document
