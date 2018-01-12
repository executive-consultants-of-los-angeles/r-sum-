"""Layout module."""
from docx.shared import Cm


def set_layout(document):
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
