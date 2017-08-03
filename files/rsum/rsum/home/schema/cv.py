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
        cv_i = CV.objects.all()
        if not cv_i.exists():
            #cv_f = open('/srv/rsum/cvs/abridged.yml')
            cv_f = open('/srv/rsum/cvs/complete.yml')
            cv_d = yaml.load(cv_f.read())
            cv_f.close()
            self.save_cv(cv_d, 'complete', 'acecv')
            cv_i = CV.objects.all()
            return cv_i
        else:
            return cv_i

    def get_cv(self):
        s = Section()
        cv = {
            'cv_name': 'complete',
            'sections': s.get_sections(
                CV.objects.filter(
                    id = 1
                )
            ),
        }
        return cv

    def save_cv(self, cv_d, name, template):
        cv = CV()
        cv.name = name 
        cv.template = template
        cv.save()

        for name, section in sorted(cv_d.items(), key = lambda t:t[1].get('id')):
            s = Section()
            s.save_section(cv, section, name)
        return cv 

    class Meta:
        app_label = "home"
        managed = True
