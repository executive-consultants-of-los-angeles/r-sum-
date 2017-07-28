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
    
    def save_sub_sections(self, cv, section):
        section_i = Section()
        section_i.cv = cv
        section_i.name = cv.section_name
        section_i.value_type = type(section)
        if type(section) == type(str()):
            section_i.value = section
            section_i.save()
        else:
            section_i.value = type(section)
            section_i.save()
            ss = SubSection()
            ss.save_projects(section, section_i)

        return Section.objects.values_list()
    
class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value_type = models.CharField(max_length=200, null=True)
    
    def save_projects(self, sub_section, section):
        if type(sub_section) == type(dict()):
            for k, v in sub_section.iteritems():
                sub_section_i = SubSection()
                sub_section_i.section = section
                sub_section_i.value_type = type(sub_section)
                sub_section_i.name = k
                sub_section_i.save()
                print(SubSection.objects.values_list())
                p = Projects() 
                p.save_project_items_dict(v, sub_section_i)
        elif type(sub_section) == type(list()):
            for c,i in enumerate(sub_section):
                sub_section_i = SubSection()
                sub_section_i.section = section
                sub_section_i.value_type = type(sub_section)
                sub_section_i.name = str(c) 
                sub_section_i.save()
                p = Projects()
                p.save_project_items_list(i, sub_section_i)
        return SubSection.objects.values_list()

class Projects(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)

    def save_project_items_dict(self, projects, sub_section):
        for k, v in projects.iteritems():
            p_i = Projects()
            p_i.sub_section = sub_section
            p_i.name = k 
            p_i.value = v
            p_i.save()
        return Projects.objects.values_list() 

    def save_project_items_list(self, projects, sub_section):
        for k,v in projects.iteritems():
            p_i = Projects()
            p_i.sub_section = sub_section
            p_i.name = k
            p_i.value = type(v)
            p_i.save()
            pil = ProjectItemsList()
            pil.save_project_dict(v, p_i)
        return Projects.objects.values_list()

class ProjectItemsList(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null = True) 

    def save_project_dict(self, project_item, project):
        for key,p_item in project_item.iteritems():
            pil_i = ProjectItemsList()
            pil_i.project = project
            pil_i.name = key
            if type(p_item) == type(dict()):
                pil_i.value = type(p_item)
                pil_i.save()
                projectitem = ProjectItem()
                projectitem.save_project_item(p_item, pil_i)
            else:
                pil_i.value = p_item
                pil_i.save()
        return None


class ProjectItem(models.Model):
    project_item_list = models.ForeignKey(ProjectItemsList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    value = models.CharField(max_length=200, null = True) 

    def save_project_item(self, project_item, pil):
        for k, v in project_item.iteritems():
            pi = ProjectItem()
            pi.project_item_list = pil
            pi.name = k
            pi.value = type(v)
            pi.save()
            projectlistitem = ProjectListItem()
            projectlistitem.save_list_item(v, pi)
        print(json.dumps(project_item, indent=2))
        return None


class ProjectListItem(models.Model):
    project_item = models.ForeignKey(ProjectItemList, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, null=True)

    def save_list_item(self, list_item, pi):
        for i in list_item:
            pli = ProjectListItem()
            pli.project_item = pi
            pli.value = i
            pli.save()
        print(ProjectListItem.objects.values_list()) 
        return ProjectListItem.objects.values_list() 
