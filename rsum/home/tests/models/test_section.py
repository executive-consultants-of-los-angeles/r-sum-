"""Test module for the section class."""
import json
import pytest


class TestSection:
    """Class for testing Section objects."""

    section_obj = object

    @pytest.mark.usefixtures('db')
    def test_section_instance(self, profile, section):
        """Test the create method for Section objects."""
        print(profile)
        print(section)
        if not isinstance(section, self.section_obj):
            raise AssertionError()

    @pytest.mark.usefixtures('db')
    def test_save_method(self, profile, section):
        """Test that sections save correctly."""
        self.section_obj = section
        save_content = {
            'projects': {
                'one': 'grenada',
                'two': 'the falkands'
            }
        }

        section = self.section_obj()
        section.profile = profile
        section.name = 'Tests!'
        section.content = json.dumps(save_content)
        print(profile)

        print(section)
        if not isinstance(section, self.section_obj):
            raise AssertionError()
