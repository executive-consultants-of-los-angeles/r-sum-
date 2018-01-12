

    def add_intro(self, intro, document):
        """Add introduction section.

        :param intro: Introduction to add to document.
        :type intro: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Introduction.
        :rtype: object
        """
        s = self.s
        table = document.add_table(rows=1, cols=2)
        table.cell(0, 0).width = Cm(12)

        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.cell(0, 0).add_paragraph(
            intro.get('name'),
            style='Heading 1')
        table.cell(0, 0).add_paragraph(
            intro.get('position'),
            style='Heading 2')

        table.cell(0, 1).width = Cm(4)
        table.cell(0, 1).add_picture(
            '/srv/rsum/static/{0}/img/mockup/avatar-02.png'.format(s.DIR))
        table.cell(
            0,
            1
        ).paragraphs[
            0
        ].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return document
