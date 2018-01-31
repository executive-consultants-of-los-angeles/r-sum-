"""Test module for the skills class."""
import json


class TestSkills:
    """Class for testing Skills objects."""

    floating_point = 2 / 3
    skills_obj = object

    def test_skills_instance(self, skills):
        """Test the create method for Skills objects."""
        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_calculate_experience(self, skills):
        """Test the validity of the experience calculation method."""

        if not skills:
            raise AssertionError()

        if not round(self.floating_point.real, 2):
            raise AssertionError()

    def test_calculate_skills(self, profile, skills):
        """Test that skillss save correctly."""
        skills_profile = profile.create()
        self.skills_obj = skills

        skills_data = json.loads(skills_profile.content)

        skills = self.skills_obj(skills_data[2])

        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_attributes(self, profile, skills):
        """Get a skills and test its attributes."""
        self.skills_obj = skills
        profile = profile.create()
        skills_set = json.loads(profile.content[2])

        for item in skills_set:
            json_content = json.loads(item.content)
            if not isinstance(item.name, str):
                raise AssertionError()

            if not isinstance(json_content, (dict, list)):
                raise AssertionError()

            if not isinstance(item.profile, profile):
                raise AssertionError()
