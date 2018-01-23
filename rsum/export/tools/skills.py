"""Skills section module."""


class Skills(object):
    """Class for skills section object."""

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
