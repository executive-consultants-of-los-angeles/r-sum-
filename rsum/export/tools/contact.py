

    def add_contact(self, contact, document):
        """Add contact section.

        :param [dict(str, str)] contact:
            Contact section for current document.
        :param object document: Current document.
        :return: Current document with Contact section.
        :rtype: object
        """
        document.add_paragraph(contact.get('title'), style='Heading 3')
        p = document.add_paragraph(contact.get('message'), style='Normal')
        p.paragraph_format.space_after = 0
        t = document.add_table(rows=2, cols=6)
        p = t.cell(0, 0).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(0, 0).add_paragraph(
            'Website',
            style='Heading 4')
        p = t.cell(0, 0).add_paragraph(
            contact.get('web'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(0, 1).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(0, 1).add_paragraph(
            'Email',
            style='Heading 4')
        p = t.cell(0, 1).add_paragraph(
            contact.get('email'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(1, 0).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(1, 0).add_paragraph(
            'Phone',
            style='Heading 4')
        p = t.cell(1, 0).add_paragraph(
            contact.get('phone'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = t.cell(1, 1).paragraphs[0]
        p.paragraph_format.line_spacing = 0
        t.cell(1, 1).add_paragraph('Location', style='Heading 4')
        p = t.cell(1, 1).add_paragraph(
            contact.get('location'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        return document
