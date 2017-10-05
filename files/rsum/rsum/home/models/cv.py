#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module containing the CV Model class."""
from __future__ import unicode_literals
from __future__ import print_function

import datetime
import json
import socket
import yaml

from django.db import models
from django.conf import settings
from section import Section


class CV(models.Model):
    """The CV Model class.

    .. attribute:: name

       Name of the current CV.

    .. attribute:: template

        Template path containing static files for CV.

        .. warning:: I believe this is not used and should be removed.

    """
    name = models.CharField(max_length=200)
    template = models.CharField(max_length=200, null=True)

    @classmethod
    def create(cls, name='default'):
        """Class method to handle creation of CV objects for testing.
        
        :param cls: The CV class.
        :type cls: :obj:`home.models.cv.CV`
        :param str name: Name of the cv.
        :return: Reference to the created CV.
        :rtype: :obj:`home.models.cv.CV`
        """
        cv = cls(name=name)
        cv.save()
        return cv 

    def check_sections(self, *args, **kwargs):
        """Check to see if the current CV Model already has sections.

        :return: ID of the current CV object.
        :rtype: int
        """
        prefix = '/srv/rsum/cvs/'
        with open(
            prefix+settings.DIR+'/'+settings.CV+'.yml',
            'r'
        ) as cv_file:
            cv_dict = yaml.load(cv_file.read())
        self.id = self.save_cv(
            cv_dict, 
            name=settings.CV,
            template=settings.OWNER
        )
        return self.id 

    def get_cv(self, cv_id=1, *args, **kwargs):
        """Get the CV at location cv_id.

        :param cv_id: ID of a CV object to retrieve.
        :type cv_id: int
        :return: Filled out CV. 
        :rtype: dict(str, str)
        """
        s = Section()
        cv = {
            'name': kwargs.get('name_of_cv'),
            'sections': s.get_sections(
                CV.objects.filter(
                    id=cv_id
                )
            ),
        }
        return cv

    def get_experience(self, context):
        """Get the experience section for related value in context.

        :param context: Dictionary of existing cv context.
        :type context: dict(str, str)
        :return: Context for CV updated with assembled Experience section.
        :rtype: [dict(str, str)]
        """
        experience_list = context.get('cv')[4].get('content')[1:]
        for k, v in enumerate(experience_list):
            for p, i in v.get(
                'content'
            )[-1].get('content').get('projects').iteritems():
                if (
                    isinstance(i, str) or
                    isinstance(i, unicode)
                ):
                    j = i.strip("[").strip("]").split(", ")
                    experience_list[k].get(
                        'content'
                    )[5].get('content').get('projects').update({p: []})
                    for l in j:
                        l = l.replace("'", '')
                        experience_list[k].get(
                            'content'
                        )[5].get('content').get('projects').get(p).append(l)
        return experience_list

    def get_skills(self, context):
        """Get Skills section for related value in context.

        :param context: Existing context for current CV.
        :type context: dict(str, str)
        :return: Skills section of CV.
        :rtype: dict(str, str) 
        """
        skills = context.get('cv')[2].get('content')
        skillset = {}

        start_career = SubSection.objects.filter(
            section_id=3
        ).filter(
            name='start'
        ).values()[0].get('content')
        current_year = float(datetime.date.today().strftime("%Y"))
        years_career = float(current_year) - float(start_career)

        # I failed algorithms in college. 
        for index, skill in enumerate(skills):
            for content in skill.get('content'):
                if content.get('name') == 'name':
                    skillset.update({
                        content.get('content'): {
                            'index': index,
                        }
                    })

        for name, value in skillset.iteritems():
            for content in skills[value.get('index')].get('content'):
                if content.get('name') == 'start':
                    start_skill = float(content.get('content'))
                    years_skill = current_year - start_skill
                    experience_value = years_skill / years_career * 100
                    experience_string = "{0} year(s)".format(int(years_skill))

                    skillset.get(name).update({
                        'experience_value': experience_value,
                        'experience_string': experience_string,
                    })
                elif (
                    content.get('name') != 'id' and 
                    content.get('name') != 'start' and 
                    content.get('name') != 'name'
                ):
                    sub_name = content.get(
                        'content'
                    ).get(
                        content.get('name')
                    ).get(
                        'name'
                    )

                    start_skill = int(content.get(
                        'content'
                    ).get(
                        content.get('name')
                    ).get(
                        'start'
                    ))

                    years_skill = float(current_year) - float(start_skill)

                    experience_value = years_skill / years_career * 100
                    experience_string = "{0} year(s)".format(int(years_skill))

                    # Assemble the skill set to be returned.
                    skillset.get(name).update({
                        content.get('name'): {
                            'experience_string': experience_string,
                            'name': sub_name,
                            'experience_value': experience_value, 
                        }
                    })
        return skillset

    def get_values(self, context):
        """Get values section for related value in context.

        :param context: Exis5ting context for CV object.
        :type context: dict(str, str) 
        :return: List of dictionaries containing the Values section.
        :rtype: [dict(str, str)]
        """
        values = {}
        values_list = context.get(
            'cv'
        )[3].get('content')[1].get('content')
        for i in values_list:
            name = i.get('content').items()[0][0]
            content = i.get('content').items()[0][1]
            values.update({name: content})

        values_list = []
        for value in sorted(
            values.items(),
            key=lambda t: t[1].get('id')
        ):
            values_list.append(value)
        return values_list

    def save_cv(self, cv_d, name='default', *args, **kwargs):
        """Save the current CV model.

        :param cv_d: Data to be saved into current CV.
        :type cv_d: dict(str, str) 
        :param name: Name of current CV.
        :type name: str
        :return: ID of saved CV.
        :rtype: int
        """
        cv = CV()
        cv.name = name 
        cv.template = kwargs.get('template')
        cv.save()

        for name, section in sorted(
            cv_d.items(),
            key=lambda t: t[1].get('id')
        ):
            s = Section()
            s.save_section(cv, section, name)

        return getattr(cv, 'id')

    class Meta:
        app_label = "home"
        managed = True
