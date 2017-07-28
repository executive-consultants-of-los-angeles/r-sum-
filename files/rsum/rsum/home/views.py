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

    cv = cv_i.get_cv(1)
    
    print(cv) 

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
                            p_entries = list(pe.get_entry(p_value.get('id'))) 
                            sections[i].get('subsections')[index].get('value')[p_index].update({'value': p_entries})
                            for pe_index, pe_value in enumerate(p_entries):
                                el = models.EntryListItem()
                                el_items = list(el.get_list_item(pe_value.get('id')))                              
                                sections[i].get('subsections')[index].get('value')[p_index].get('value')[pe_index].update({'value': el_items})


    context = {
        'sections': sections 
    }

    return render(request, 'home/index.html', {})
