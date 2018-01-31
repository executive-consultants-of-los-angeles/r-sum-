"""Test module for the skills class."""
import datetime
import json


class TestSkills:
    """Class for testing Skills objects."""

    current_year = float(datetime.date.today().strftime('%Y'))
    start_year = 1980
    floating_point = 2 / 3
    skills_obj = object
    skills = None

    def test_skills_instance(self, skills):
        """Test the create method for Skills objects."""
        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_calculate_experience(self, skills):
        """Test the validity of the experience calculation method."""
        self.skills = skills.skills_data.get('skills')
        self.start_year = self.skills.pop('start', None)
        skills.career_length = (
            float(self.current_year) - float(self.start_year)
        )

        for name, skill in self.skills.items():
            experience = skills.calculate_experience(skill)

            if not isinstance(name, str):
                raise AssertionError()

            if experience.get('value') > 100 or experience.get('value') < 0:
                raise AssertionError()

            if not isinstance(experience.get('string'), str):
                raise AssertionError()

            if not isinstance(experience.get('value'), float):
                raise AssertionError()

    def test_calculate_skills(self, skills):
        """Test that skillss save correctly."""
        self.skills = skills.skills_data.get('skills')
        self.start_year = self.skills.pop('start', None)
        skills.career_length = (
            float(self.current_year) - float(self.start_year)
        )

        result = skills.calculate_skills()

        print(result)

        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_calculate_sub_skills(self, profile, skills):
        """Get a skills and test its attributes."""
        self.skills_obj = skills
        profile = profile.create()
        skills_set = json.loads(profile.content)

        for name, item in skills_set[2].items():
            if name != 'skills':
                raise AssertionError()

            if not isinstance(item.get('name'), str):
                raise AssertionError()

            if not isinstance(item, (dict, list)):
                raise AssertionError()

            if not isinstance(item.get('profile'), profile):
                raise AssertionError()
