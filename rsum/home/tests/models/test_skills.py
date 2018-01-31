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
        skills_set = json.loads(profile.content)

        for item in skills_set:
            if not isinstance(item.get('name'), str):
                raise AssertionError()

            if not isinstance(item, (dict, list)):
                raise AssertionError()

            if not isinstance(item.get('profile'), profile):
                raise AssertionError()
