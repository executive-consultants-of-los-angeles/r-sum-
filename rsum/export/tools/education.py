

    def add_education(self, education, document):
        """Add education section.

        :param [dict(str, str)] education:
            Education section for current document.
        :param object document: Current document.
        :return: Current document with Educaiton section.
        :rtype: object
        """
        s = self.s
        p = document.add_paragraph(
            'Education',
            style='Heading 3')
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_after = 0
        p.paragraph_format.page_break_before = True
        document.add_picture(
            '/srv/rsum/static/{0}/img/1920x1080/01.jpg'.format(
                s.DIR),
            width=Cm(4))
        p = document.add_paragraph(
            education.get('name'),
            style='Heading 4')
        p.paragraph_format.space_before = 0
        p = document.add_paragraph(
            education.get('studies'),
            style='Heading 5')
        p.paragraph_format.space_before = 0
        p = document.add_paragraph(
            "{0}, {1}".format(
                education.get('location'),
                education.get('duration')),
            style='Heading 6')
        p.paragraph_format.space_before = 0
        for name, project in education.get('projects').items():
            p = document.add_paragraph(
                name.title(),
                style='List Bullet')
            for item in project:
                p = document.add_paragraph(
                    item,
                    style='List Bullet 2')
        return document
