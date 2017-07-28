#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render

import json
import models

# Create your views here.

def index(request):
    sections = []
    
    cv_i = models.CV()
    cv_i.check_sections()
    for i in range(1,len(models.Section.objects.all())+1):
        s = models.Section()
        sections.append(
            s.get_section(i)
        )


    for i in range(0,len(sections)):
        ss = models.SubSection()
        subsections = list(ss.get_sub_section(sections[i].get('id')))
        if len(subsections) > 0:
            sections[i].update({'subsections': subsections})
            for index, value in enumerate(subsections):
                p = models.Project()
                projects = list(p.get_projects(value.get('id')))[0]
                if projects.get('value') != u"<type 'dict'>":
                    sections[i].get('subsections')[index].update({'value':projects})
                else:
                    pi = models.ProjectItems()
                    p_items = list(pi.get_project_items(projects.get('id')))
                    sections[i].get('subsections')[index].update({'value':p_items})
                    for p_index, p_value in enumerate(p_items):
                        if p_value.get('value') != u"<type 'dict'>":
                            sections[i].get('subsections')[index].get('value')[p_index].update({'value': p_value}) 
                        else:
                            pe = models.ProjectEntry()
                            p_entries = pe.get_entry(p_value.get('id')) 
                            print(p_entries) 

    context = {
        'sections': models.Section.objects.all().__dict__,
        'sub_sections': models.SubSection.objects.all().__dict__,
    }

    return render(request, 'home/index.html', {})
