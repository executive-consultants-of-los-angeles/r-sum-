"""Test module for the section class."""
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
    def test_section_save(self, profile, section):
        """Test that sections save correctly."""
        self.section_obj = section

        section = self.section_obj()
        print(profile)

        print(section)
        if not isinstance(section, self.section_obj):
            raise AssertionError()

