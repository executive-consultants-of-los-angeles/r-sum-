#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models
from section import Section


class CV(models.Model):
    name = models.CharField(max_length=200)
    template = models.CharField(max_length=200, null=True)

    def check_sections(self):
        cv_i = CV.objects.all()
        if not cv_i.exists():
            cv_f = open('/srv/rsum/cvs/abridged.yml')
            cv_d = yaml.load(cv_f.read())
            self.save_cv(cv_d.get('cv'))
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

    def save_cv(self, cv_d):
        cv_i = CV()
        cv_i.name = 'abridged' 
        cv_i.save()

        for name, section in cv_d.iteritems():
            s = Section()
            s.save_section(cv_i, section, name)

        return CV.objects.values_list() 

    class Meta:
        app_label = "home"
        managed = True
