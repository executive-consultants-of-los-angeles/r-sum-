"""Values export object module."""


class Values(object):
    """Class for Values export object."""

    name = None
    document = None

    def save(self, name, section, document, graphics=True):
        """Get intro."""
        self.name = name
        self.document = document
        section = self.name
        return document

    def save_with_graphics(self, name, section, document):
        """Get intro."""
        self.name = name
        self.document = document
        section = self.name
        return document
