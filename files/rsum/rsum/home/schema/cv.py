#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from collections import OrderedDict

import yaml
import json

from django.db import models
from section import Section


class CV(models.Model):
    name = models.CharField(max_length=200)
    template = models.CharField(max_length=200, null=True)

    def check_sections(self):
        # cv_f = open('/srv/rsum/cvs/abridged.yml')
        cv_f = open('/srv/rsum/cvs/complete.yml')
        cv_d = yaml.load(cv_f.read())
        self.save_cv(cv_d, 'complete', template='acecv')
        return CV.objects.values() 

    def get_cv(self):
        s = Section()
        cv = {
            'name': 'complete',
            'sections': s.get_sections(
                CV.objects.filter(
                    id=9 
                )
            ),
        }
        return cv

    def get_experience(self, context):
        experience_list = context.get('cv')[4].get('experience').get('content')[1:]
        for k, v in enumerate(experience_list):
            # print(json.dumps(v,indent=1))
            for p, i in v.get(
                'content'
            )[5].get('content').get('projects').iteritems():
                j = i.strip('[').strip(']').split("', '")
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
        print(context)
        skills = context.get('cv')[2].get('skills').get('content')
        skillset = {}

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
                if content.get('name') == 'competence':
                    skillset.get(name).update({
                        'competence': content.get('content'),
                    })
                elif content.get('name') != 'id' and content.get('name') != 'name':
                    skillset.get(name).update({
                        content.get('name'): {
                            'experience': content.get(
                                'content'
                            ).get(
                                content.get('name')
                            ).get('experience'),
                            'name': content.get(
                                'content'
                            ).get(
                                content.get('name')
                            ).get('name'),
                            'competence': content.get(
                                'content'
                            ).get(
                                content.get('name')
                            ).get('competence'),
                        }
                    })
        return skillset

    def get_values(self, context):
        values = {}
        values_list = context.get(
            'cv'
        )[3].get('values').get('content')[1].get('content')
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

        return cv

    def sort_sections(self, cv):
        sections = []
        for section in sorted(
            cv.get('sections').items(),
            key=lambda t: t[1].get('id')
        ):
            sections.append({section[0]: section[1]})
        return sections

    class Meta:
        app_label = "home"
        managed = True
