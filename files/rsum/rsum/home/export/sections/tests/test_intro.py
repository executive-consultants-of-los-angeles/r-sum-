"""Testing add introduction."""
import docx

import home.export.word as word
import home.export.sections.intro as intro
import home.models.section as section


class TestIntro(object):
    """Text intro class."""
    document = docx.Document()
    sections = section.Section.objects.all()

    def test_intro(self):
        """Assert results of introduction method."""
        
        result = intro.introduction(self.document)

        assert result is not None
