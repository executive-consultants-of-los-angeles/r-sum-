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
        print(json.dumps(skills_data, indent=2))

        skills = self.skills_obj(skills_data)
        print(skills)

        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_attributes(self, profile, skills):
        """Get a skills and test its attributes."""
        self.skills_obj = skills
        profile.create()
        skillss = self.skills_obj.objects.all()

        for item in skillss:
            json_content = json.loads(item.content)
            if not isinstance(item.name, str):
                raise AssertionError()

            if not isinstance(json_content, (dict, list)):
                raise AssertionError()

            if not isinstance(item.profile, profile):
                raise AssertionError()
