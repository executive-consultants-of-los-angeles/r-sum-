

    def add_experience(self, experience, document):
        """Add experience section.

        :param [dict(str, str)] experience:
            Experience section to add to document.
        :param object document: Document to update.
        :return: Document updated with Experience section.
        :rtype: object
        """
        s = self.s
        del experience[0]
        p = document.add_paragraph(
            'Experience',
            style='Heading 3')
        t = document.add_table(rows=1, cols=3)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for index, value in enumerate(experience):
            if index % 3 == 0:
                t.add_row()

            for name, item in value.items():
                row = (index % 9) / 3
                col = index % 3
                if (
                        index % 9 == 0 and
                        index > 0
                ):
                    t = document.add_table(rows=1, cols=3)
                    t.alignment = WD_TABLE_ALIGNMENT.CENTER

                if (
                        index % 18 == 0
                        and index > 17
                ):
                    document.add_page_break()
                    t = document.add_table(rows=1, cols=3)
                    t.alignment = WD_TABLE_ALIGNMENT.CENTER
                p = t.cell(row, col).paragraphs[0]
                p.paragraph_format.line_spacing = 0.0
                t.cell(row, col).add_picture(
                    '/srv/rsum/static/{}/img/970x647/{}.jpg'.format(
                        s.DIR,
                        index+1
                    ),
                    width=Cm(4.8)
                )
                p = t.cell(row, col).paragraphs[1]
                p.paragraph_format.space_after = 0

                p = t.cell(row, col).add_paragraph(
                    item.get('position'),
                    style='Heading 4')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
                p = t.cell(row, col).add_paragraph(
                    item.get('company'),
                    style='Heading 5')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = 0
                p = t.cell(row, col).add_paragraph(
                    "{0}, {1}".format(
                        item.get('location'),
                        item.get('duration')),
                    style='Heading 6')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = 0
                t = self.add_projects(item.get('projects'), t, row, col)
        p = document.add_paragraph('')
        p.paragraph_format.line_spacing = 0
        return document

    def add_projects(self, projects, table, row, col):
        """Add projects to experience section.

        :param [dict(str, str)] projects:
            Projects for a portion of Experience section.
        :param object table: Table from current document.
        :param int row: Index of current row.
        :param int col: Index of current col.
        :return: Updated Projects table.
        :rtype: object
        """
        for name, project in projects.items():
            p = table.cell(row, col).add_paragraph(
                name.replace('_', ' ').title(),
                style='List Bullet')
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_after = 0
            for item in project:
                p = table.cell(row, col).add_paragraph(
                    item,
                    style='List Bullet 2')
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_after = 0
        return table
