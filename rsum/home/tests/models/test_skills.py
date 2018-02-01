"""Test module for the skills class."""
import copy
import datetime


class TestSkills:
    """Class for testing Skills objects."""

    current_year = float(datetime.date.today().strftime('%Y'))
    start_year = 1980
    floating_point = 2 / 3
    skills_obj = object

    def test_skills_instance(self, skills):
        """Test the create method for Skills objects."""
        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_calculate_skills(self, skills):
        """Test that skillss save correctly."""
        local_skills = copy.copy(skills)
        local_skill_data = local_skills.skills_data.get('skills')

        prepared_skills = skills.calculate_skills(local_skill_data)
        for name, skill in prepared_skills.items():
            if not isinstance(name, str):
                raise AssertionError()

            if not isinstance(skill, dict):
                raise AssertionError()

        if not isinstance(skills, self.skills_obj):
            raise AssertionError()

    def test_calculate_experience(self, skills):
        """Test the validity of the experience calculation method."""
        local_skills = skills.skills_data.get('skills')
        self.start_year = local_skills.get('start')

        for name, skill in local_skills.items():
            experience = skills.calculate_experience(skill)

            if not isinstance(name, str):
                raise AssertionError()

            if experience.get('value') > 100 or experience.get('value') < 0:
                raise AssertionError()

            if not isinstance(experience.get('string'), str):
                raise AssertionError()

            if not isinstance(experience.get('value'), float):
                raise AssertionError()
