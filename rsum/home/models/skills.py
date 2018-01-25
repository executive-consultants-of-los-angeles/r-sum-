"""Module for handling skils calculation."""
import datetime


class Skills(object):
    """Skills class for Skills objects."""

    skills = {}
    sub_skills = {}
    current_year = float(datetime.date.today().strftime("%Y"))
    career_length = float(0)

    def __init__(self, skills):
        """Initialize the Skills class."""
        self.skills = skills

    def calculate_skills(self):
        """Calculate necessary values for the skills progress bars.

        :param skills: The unmodified skills section.
        :type skills: OrderedDict
        :return: An updated Skills section with missing values filled in.
        :rtype: OrderedDict
        :raises: ValueError
        """
        skills = self.skills
        begin = skills.get('start')
        self.career_length = float(self.current_year) - float(begin)

        for name, skill in skills.items():
            if name != 'start':
                start_skill = float(skill.get('start'))
                years_skill = self.current_year - start_skill
                experience_value = years_skill / self.career_length * 100
                experience_string = "{0} year(s)".format(int(years_skill))

                skills = self.calculate_sub_skills(name, skill.items(), skills)

                skills.update({
                    name: {
                        'name': skills.get(name).get('name'),
                        'start': skills.get(name).get('start'),
                        'experience_value': experience_value,
                        'experience_string': experience_string,
                    }
                })
        return skills

    def calculate_sub_skills(self, name, sub_skills, skills):
        """Calculate sub skills and return the result."""
        # I don't much like nested for loops, but it's the only way.
        for sub_name, sub_skill in sub_skills.items():
            if (
                    not isinstance(sub_skill, str) and
                    not isinstance(sub_skill, int)
            ):
                start_sub = float(sub_skill.get('start'))
                years_sub = self.current_year - start_sub
                sub_experience_value = years_sub / self.career_length * 100
                sub_experience_string = (
                    "{0} year(s)".format(int(years_sub))
                )

                skills.get(name).update({
                    sub_name: {
                        'name': sub_skill.get('name'),
                        'start': sub_skill.get('start'),
                        'experience_value': sub_experience_value,
                        'experience_string': sub_experience_string,
                    }
                })
