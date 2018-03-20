"""Skills section module."""
# pylint: disable=no-name-in-module
import datetime


class Skills(object):
    """Class for skills section object."""

    name = None
    graphics = False
    document = None
    sub_skills = None
    current_year = float(datetime.datetime.now().strftime('%Y'))

    def save(self, section, document, graphics):
        """Add skills section.

        :param skills: Skills section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Skills.
        :rtype: object
        """
        self.document = document
        self.graphics = graphics
        document = self.get_skills(section, document)
        return document

    def get_skills(self, section, document):
        """Add skills section.

        :param skills: Skills section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Skills.
        :rtype: object
        """
        skills = section

        document.add_paragraph('Skills', style='Heading 3')
        table = document.add_table(rows=1, cols=2)
        index = 1
        for skill_name, skill in skills.items():
            if isinstance(skill, dict):
                experience = int(self.current_year) - int(skill.get('start'))
                experience = '{0} year(s)'.format(str(experience))
                output_name = skill_name.replace('_', ' ').title()
                table.cell(0, index % 2).add_paragraph(
                    "{} \t || {}".format(output_name, experience),
                    "List Bullet"
                )
                self.sub_skills = skill
                table = self.get_sub_skills(skill, table, index)
            index = index + 1
        return document

    def get_sub_skills(self, sub_skills, table, index):
        """Add sub skills for skills section.

        :param sub_skills: The collection of sub skills to add.
        :param table: The table to update.
        :param index: Current iteration of parent loop.
        :return: Updated table.
        """
        for sub in sub_skills.items():
            if isinstance(sub[1], dict):
                experience = (
                    int(self.current_year) - int(sub[1].get('start')))
                experience = '{0} year(s)'.format(str(experience))
                table.cell(0, index % 2).add_paragraph(
                    "{} \t || {}".format(
                        sub[1].get('name'), experience),
                    "List Bullet 2"
                )
        return table
