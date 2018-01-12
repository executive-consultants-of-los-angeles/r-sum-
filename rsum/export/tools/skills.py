"""Skills module."""


def add_skills(self, skills, document):
    """Add skills section.

    :param skills: Skills section to add to document.
    :type summary: [dict(str, str)]
    :param document: Current document.
    :type document: object
    :return: Document updated with Skills.
    :rtype: object
    """
    current_year = datetime.datetime.now().strftime("%Y")

    t = document.tables[1]
    t.cell(0, 1).add_paragraph('Skills', style='Heading 3')
    t_sub = t.cell(0, 1).add_table(rows=1, cols=2)
    t.cell(0, 1).tables[0].columns[0].width = Cm(7)
    index = 1
    for name, skill in skills.items():
        if isinstance(skill, dict):
            experience = int(current_year) - int(skill.get('start'))
            experience = '{0} year(s)'.format(str(experience))
            name = skill.get('name').replace('_', ' ').title()

            # Add a row to the sub table.
            t_sub.add_row()
            t_sub.cell(index-1, 0).text = name
            p = t_sub.cell(index-1, 0).paragraphs[0]
            p.style = 'Skill'
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = 0
            t_sub.cell(index-1, 1).text = experience

            p = t_sub.cell(index-1, 1).paragraphs[0]
            p.style = 'Skill'
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = 0
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            t_sub = self.add_sub_skills(skill, t_sub, index-1)
        index = index + 1
    return document

def add_sub_skills(self, subs, ts, ts_index):
    """Add sub skills to skills section.

    :param subs: Sub skills to add to document.
    :type subs: [dict(str, str)]
    :param object ts: Table cell to update.
    :param int ts_index: Index for current table cell.
    :return: Document updated with sub skills.
    :rtype: object
    """
    current_year = float(datetime.datetime.now().strftime("%Y"))
    sub_table = ts.cell(ts_index, 0).add_table(rows=1, cols=2)
    index = 0
    for name, sub in subs.items():
        if isinstance(sub, dict):
            experience = int(current_year) - int(sub.get('start'))
            experience = '{0} year(s)'.format(str(experience))
            if index == 0:
                sub_table.cell(0, 0).text = sub.get('name')
                sub_table.cell(0, 1).text = experience
                sub_table.cell(0, 0).width = Cm(5)
            else:
                sub_table.add_row()
                sub_table.cell(index, 0).text = sub.get('name')
                sub_table.cell(index, 0).width = Cm(1)
                sub_table.cell(index, 1).text = experience
            p = sub_table.cell(index, 0).paragraphs[0]
            p.style = 'Sub Skill'
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = 0
            p = sub_table.cell(index, 1).paragraphs[0]
            p.style = 'Sub Skill'
            p.paragraph_format.line_spacing = 1.0
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p.paragraph_format.space_after = 0
            index = index + 1
    return ts
