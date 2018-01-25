"""Values export object module."""


class Values(object):
    """Class for Values export object."""

    name = None
    document = None

    def save(self, name, section, document):
        """Get intro."""
        self.name = name
        self.document = document
        section = self.name
        print(section)

        print(document)
        return document

    def organize(self):
        """Organize something."""
        return self
