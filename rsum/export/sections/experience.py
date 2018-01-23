"""Experience module."""
# pylint: disable=no-member
from django.conf import settings as django_settings
from docx.shared import Cm
from docx.enum.table import WD_TABLE_ALIGNMENT


class Experience(object):
    """Export Experience object."""

    name = None
    document = None
    projects = None
    settings = django_settings

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
        projects = self.projects
        for project_name, project in projects.items():
            paragraph = table.cell(row, col).add_paragraph(
                project_name.replace('_', ' ').title(),
                style='List Bullet')
            paragraph.paragraph_format.line_spacing = 1.0
            paragraph.paragraph_format.space_after = 0
            for item in project:
                paragraph = table.cell(row, col).add_paragraph(
                    item,
                    style='List Bullet 2')
                paragraph.paragraph_format.line_spacing = 1.0
                paragraph.paragraph_format.space_after = 0
        return table

    def save(self, name, section, document):
        """Add experience section.

        :param [dict(str, str)] experience:
            Experience section to add to document.
        :param objectable document: Documentable to update.
        :return: Documentable updated with Experience section.
        :rtype: object
        """
        experience = section
        self.name = name

        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0.0
        paragraph.paragraph_format.page_break_before = True
        paragraph = document.add_paragraph(
            'Experience', style='Heading 3')

        table = document.add_table(rows=1, cols=3)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for index, value in enumerate(experience):
            if index % 3 == 0:
                table.add_row()
            self.document = document
            document = self.set_tables(table=table, value=value, index=index)

        paragraph = document.add_paragraph('')
        paragraph.paragraph_format.line_spacing = 0
        print(name)
        print(document)
        return document

    def set_tables(self, **dargs):
        """Set tables for the experience section."""
        self.document = (
            self.prep_tables(
                table=dargs.get('table'),
                value=dargs.get('value'), index=dargs.get('index')
            )
        )
        document = self.document
        return document

    def prep_tables(self, **dargs):
        """Prepare tables."""
        for item in dargs.get('value'):
            index = dargs.get('index')
            row = (index % 9) / 3
            col = index % 3
            if (
                    index % 9 == 0 and
                    index > 0
            ):
                table = self.document.add_table(rows=1, cols=3)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER

            self.document = self.build_tables(table=dargs.get('table'),
                                              index=index, row=row,
                                              col=col, item=item)
            document = self.document
            return document

    def build_tables(self, **dargs):
        """Construct tables."""
        document = self.document
        index = dargs.get('index')
        row = dargs.get('row')
        col = dargs.get('col')
        settings = self.settings
        item = dargs.get('item')
        table = dargs.get('table')
        if (index % 18 == 0 and index > 17):
            document.add_page_break()
            table = document.add_table(rows=1, cols=3)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
        paragraph = table.cell(int(row), int(col)).paragraphs[0]
        paragraph.paragraph_format.line_spacing = 0.0
        table.cell(int(row), int(col)).add_picture(
            'static/profiles/{}/img/970x647/{}.jpg'.format(
                settings.DIR,
                index+1
            ),
            width=Cm(4.8)
        )
        self.document = self.finish_tables(table=table, row=row,
                                           col=col, item=item)
        return document

    def finish_tables(self, **dargs):
        """Complete process started in calling methond."""
        document = self.document
        table = dargs.get('table')
        row = int(dargs.get('row'))
        col = int(dargs.get('col'))
        item = dargs.get('item')
        paragraph = table.cell(row, col).paragraphs[1]
        paragraph.paragraph_format.space_after = 0

        paragraph = table.cell(row, col).add_paragraph(
            item, style='Heading 4')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_after = 0
        paragraph = table.cell(row, col).add_paragraph(
            item, style='Heading 5')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_before = 0
        paragraph = table.cell(row, col).add_paragraph(
            "{0}, {1}".format(item, item),
            style='Heading 6')
        paragraph.paragraph_format.line_spacing = 1.0
        paragraph.paragraph_format.space_before = 0
        return document
