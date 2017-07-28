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
            cv_f = open('/srv/rsum/cv.yml')
            cv_d = yaml.load(cv_f.read())        
            self.save_sections(cv_d.get('cv'))

    def save_sections(self, cv_d):
        for k, v in cv_d.iteritems():
            current = CV()
            current.section_name = k 
            current.save()

            s = Section()
            s.save_sub_sections(current, v)
        return None


class Section(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='section')
    value = models.CharField(max_length=200, null=True) 
    value_type = models.CharField(max_length=200, null=True) 
    
    def save_sub_sections(self, cv, section):
        section_i = Section()
        section_i.cv = cv
        section_i.name = cv.section_name
        section_i.value_type = type(section)
        if type(section) == type(str()):
            section_i.value = section
        else:
            ss = SubSection()
            ss.save_projects(section, section_i)
        section_i.save()

        return Section.objects.values_list()
    
class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)
    
    def save_projects(self, sub_section, section):
        if type(sub_section)) == type(dict()):
            sub_section_i = SubSection()
            sub_section_i.section = section
            print(sub_section)
            p = Projects() 
        elif type(sub_section)) == type(list()):
            print(type(sub_section))
            print(json.dumps(sub_section, indent=2))


class Projects(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE)

    def save_project_items_list(self):
        return None
    

class ProjectItemsList(models.Model):
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class ProjectItem(models.Model):
    project_item_list = models.ForeignKey(ProjectItemsList, on_delete=models.CASCADE)
    value = models.CharField(max_length=200) 
