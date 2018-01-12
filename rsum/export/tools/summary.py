

    def add_summary(self, summary, document):
        """Add summary section.

        :param summary: Summary section to add to document.
        :type summary: [dict(str, str)]
        :param document: Current document.
        :type document: object
        :return: Document updated with Summary.
        :rtype: object
        """
        s = self.s
        t = document.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER

        t.cell(0, 0).width = Cm(6)
        t.cell(0, 0).add_picture(
            '/srv/rsum/static/{0}/img/500x700/02.png'.format(s.DIR),
            width=Cm(5))

        t.cell(0, 1).add_paragraph('Summary', style='Heading 3')
        t.cell(0, 1).add_paragraph(summary.get('content'), style='Normal')
        p = t.cell(0, 1).paragraphs[1]
        p.paragraph_format.line_spacing = 1.0
        t.cell(0, 1).width = Cm(10)
        p = t.cell(0, 0).paragraphs[0]
        p.paragraph_format.line_spacing = 0.0
        p = t.cell(0, 1).paragraphs[0]
        p.paragraph_format.line_spacing = 0.0
        return document

