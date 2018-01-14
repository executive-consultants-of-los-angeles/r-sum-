"""Test module for the section class."""
import json


class TestSection:
    """Class for testing Section objects."""

    section_obj = object

    def test_section_instance(self, section):
        """Test the create method for Section objects."""
        if not isinstance(section, self.section_obj):
            raise AssertionError()

    def test_save_method(self, profile, section):
        """Test that sections save correctly."""
        section_profile = profile.create()
        self.section_obj = section
        save_content = {
            'projects': {
                'one': 'grenada',
                'two': 'the falkands'
            }
        }

        section = self.section_obj()
        section.profile = section_profile
        section.name = 'Tests!'
        section.content = json.dumps(save_content)
        section.save()

        if section.id != 8:
            raise AssertionError()

        if not isinstance(section, self.section_obj):
            raise AssertionError()

    def test_attributes(self, profile, section):
        """Get a section and test its attributes."""
        self.section_obj = section
        profile.create()
        sections = self.section_obj.objects.all()

        for item in sections:
            json_content = json.loads(item.content)
            if not isinstance(item.name, str):
                raise AssertionError()

            if not isinstance(json_content, (dict, list)):
                raise AssertionError()

            if not isinstance(item.profile, profile):
                raise AssertionError()
