#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models


# Create your models here.
class CV(models.Model):
    section_name = models.CharField(max_length=200)

    def check_sections(self):
        cv_i = CV.objects.all()
        if not cv_i.exists():
            print('load it up!')
            cv_f = open('/srv/rsum/cv.yml')
            cv_d = yaml.load(cv_f.read())        
            print(json.dumps(cv_d.get('cv'), indent=2))
            self.save_sections(cv_d.get('cv'))

    def save_sections(self, cv_d):
        print(json.dumps(cv_d, indent=2))
        for k, v in cv_d.iteritems():
            print(k)
            print(json.dumps(v, indent=2))
            current = CV()
            current.section_name = k 
            current.save()

            s = Section()
            s.save_sub_sections(current, v)
        return None


class Section(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    
    def save_sub_sections(self, cv, sub_sections):
        print(sub_sections)
    
class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    

class Projects(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE)


class ProjectItemsList(models.Model):
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class ProjectItem(models.Model):
    project_item_list = models.ForeignKey(ProjectItemsList, on_delete=models.CASCADE)
    value = models.CharField(max_length=200) 
