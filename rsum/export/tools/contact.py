"""Module for contact."""


class Contact(object):
    """Contact object class."""

    name = None
    document = None

    def save(self, name, section, document):
        """Get intro."""
        self.name = name
        self.document = document
        section = self.document
        print(section)

        return document

    def organize(self):
        """Organize something."""
        return self
