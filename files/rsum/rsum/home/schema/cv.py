#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models
from section import Section

sections_list = [
    'intro',
    'summary',
    'skills',
    'work',
    'experience',
    'education',
    'contact',
]


class CV(models.Model):
    cv_name = models.CharField(max_length=200)
    cv_order = models.CharField(max_length=200, null=True)
    cv_template = models.CharField(max_length=200, null=True)

    def check_sections(self):
        cv_i = CV.objects.all()
        if not cv_i.exists():
            cv_f = open('/srv/rsum/cvs/abridged.yml')
            cv_d = yaml.load(cv_f.read())
            self.save_cv(cv_d)
            cv_i = CV.objects.all()
            return cv_i
        else:
            return cv_i

    def get_cv(self):
        s = Section()
        cv = {
            'cv_name': 'abridged',
            'sections': s.get_sections(
                CV.objects.filter(
                    id = 1
                )
            ),
        }
        return cv

    def save_cv(self, cv):
        cv_i = CV()
        cv_i.cv_name = 'abridged' 
        cv_i.cv_order = sections_list 
        cv_i.save()

        for section in sections_list:
            s = Section()
            s.save_section(cv_i, section, cv.get('cv').get(section))

        return CV.objects.values_list() 

    class Meta:
        app_label = "home"
        managed = True
