#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models

from schema.cv import CV 
from schema.projectitem import ProjectItem

import json

# Create your views here.

def index(request):
    cv_i = CV(
        id = 1
    )

    cv_i.check_sections()
    cv = cv_i.get_cv()

    sections = []
    for section in sorted(cv.get('sections').items(), key = lambda t: t[1].get('id')):
        sections.append({section[0]: section[1]})

    context = {
        'cv': sections
    }

    values = {}
    values_list = context.get('cv')[3].get('values').get('content')[1].get('content')
    for i in values_list:
        name = i.get('content').items()[0][0]
        content = i.get('content').items()[0][1]
        values.update({name:content}) 

    values_list = []
    for value in sorted(values.items(), key = lambda t: t[1].get('id')):
        values_list.append(value)
    values = values_list
    context.get('cv')[3].get('values').get('content')[1].update({
        'content': values
    })

    experience = {}
    experience_list = context.get('cv')[4].get('experience').get('content')[1:]
    for k,v in enumerate(experience_list):
        #print(json.dumps(v,indent=1))
        for p, i in v.get('content')[5].get('content').get('projects').iteritems():
            j = i.strip('[').strip(']').split("', '")
            experience_list[k].get('content')[5].get('content').get('projects').update({p:[]})
            for l in j:
                l = l.replace("'", '')
                experience_list[k].get('content')[5].get('content').get('projects').get(p).append(l)
        #print(json.dumps(v.get('content')[5].get('content').get('projects'), indent=1))
    context.get('cv')[4].get('experience').update({
        'experience': experience_list
    })
    #print(json.dumps(context.get('cv')[3].get('values').get('content')[1], indent=1))
    #print(type(values))

    education = context.get('cv')[5].get('education').get('content')[3].get('content')[0]
    projects = education.get('content').replace("'",'').replace("[",'').replace("]",'').split(", ")
    context.get('cv')[5].get('education').update({
        'projects': projects
    })
    
    return render(request, 'home/index.html', context)
