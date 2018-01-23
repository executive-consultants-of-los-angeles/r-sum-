"""Module for education."""


class Education(object):
    """Education export object."""

    name = None
    document = None

    def save(self, name, section, document):
        """Get intro."""
        self.name = name
        self.document = document
        section = document
        print(section)

        return self

    def organize(self):
        """Organize something."""
        return self
