"""Styles module."""
# pylint: disable=no-member
from docx.shared import Pt
from docx.shared import RGBColor
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.enum.text import WD_TAB_LEADER
from docx.shared import Cm


def set_first_headings(document):
    """Set top three headings on document."""
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
    return document


def set_second_headings(document):
    """Set the second three headings."""
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
    return document


def set_list_bullets(document):
    """Set list bullet styles."""
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
    style.paragraph_format.tab_stops.add_tab_stop(
        Cm(0.1),
        alignment=WD_TAB_ALIGNMENT.LEFT,
        leader=WD_TAB_LEADER.SPACES
    )
    print(dir(style.paragraph_format))
    return document


def set_final_styles(document):
    """Define remaining styles."""
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


def set_styles(document):
    """Set styles in the Word document.

    :param object document: Current document.
    :return: Current document with correct styles.
    :rtype: object
    """
    document = set_first_headings(document)
    document = set_second_headings(document)
    document = set_list_bullets(document)
    document = set_final_styles(document)
    return document
