#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from collections import OrderedDict

import datetime
import json
import yaml

from django.db import models
from section import Section
from subsection import SubSection


class CV(models.Model):
    name = models.CharField(max_length=200)
    template = models.CharField(max_length=200, null=True)

    def check_sections(self, *args, **kwargs):
        prefix = '/srv/rsum/cvs/'
        with open(
            prefix+kwargs.get(
                'name_of_owner'
            )+'/'+kwargs.get(
                'name_of_cv'
            )+'.yml'
        , 'r') as cv_file:
            cv_dict = yaml.load(cv_file.read())
        self.id = self.save_cv(
            cv_dict, 
            name=kwargs.get('name_of_cv'), 
            template=kwargs.get('template'),
        )
        return self.id 

    def get_cv(self, cv_id=1, *args, **kwargs):
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
