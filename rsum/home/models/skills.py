"""Module for handling skils calculation."""
import copy
import datetime


class Skills:
    """Skills class for Skills objects."""

    skills_data = {}
    sub_skills = {}
    current_year = float(datetime.date.today().strftime("%Y"))
    career_length = float(0)
    start_year = float(datetime.date.today().strftime("%Y"))

    def __init__(self, skills_data):
        """Initialize the Skills class."""
        self.skills_data = skills_data

    def calculate_experience(self, skill):
        """Return experience as a percentage."""
        experience = {}
        start_skill = float(skill.get('start'))
        years_skill = self.current_year - start_skill
        experience.update({'value':
                           years_skill / self.career_length * 100})
        experience.update({'string': "{0} year(s)".format(int(years_skill))})
        return experience

    def calculate_skills(self, skills_data):
        """Calculate necessary values for the skills progress bars.

        :param skills: The unmodified skills section.
        :type skills: OrderedDict
        :return: An updated Skills section with missing values filled in.
        :rtype: OrderedDict
        :raises: ValueError
        """
        start_year = skills_data.pop('start', None)
        self.career_length = float(self.current_year) - float(start_year)

        for name, skill in skills_data.items():
            experience = self.calculate_experience(skill)

            skills_data.update({
                name: {
                    'name': (
                        skills_data.get(name).get(
                            'name').replace('_', ' ').title()
                    ),
                    'start': skills_data.get(name).get('start'),
                    'experience_value': experience.get('value'),
                    'experience_string': experience.get('string'),
                }
            })

            skills_data = self.calculate_sub_skills(
                name, skill, skills_data)
        return skills_data

    def calculate_sub_skills(self, name, sub_skills, skills_data):
        """Calculate sub skills and return the result."""
        local_sub = copy.copy(sub_skills)
        local_sub.pop('name')
        local_sub.pop('start')
        for sub_name, sub_skill in local_sub.items():
            experience = self.calculate_experience(sub_skill)

            skills_data.get(name).update({
                sub_name: {
                    'name': sub_skill.get('name'),
                    'start': sub_skill.get('start'),
                    'experience_value': experience.get('value'),
                    'experience_string': experience.get('string'),
                }
            })
        return skills_data
