"""Summary section export."""


class Summary(object):
    """Sumary section object class."""

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
