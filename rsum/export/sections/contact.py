"""Contact module."""
# pylint: disable=too-few-public-methods,unused-argument


class Contact(object):
    """Class for contact object export."""

    name = None

    def save(self, section, document, graphics):
        """Add contact section.

        :param [dict(str, str)] contact:
            Contact section for current document.
        :param object document: Current document.
        :return: Current document with Contact section.
        :rtype: object
        """
        self.name = graphics
        return document
