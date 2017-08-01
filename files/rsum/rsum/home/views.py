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

    #print(json.dumps(context.get('cv')[3],indent=1))
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
    #print(json.dumps(context.get('cv')[3].get('values').get('content')[1], indent=1))
    #print(type(values))

    return render(request, 'home/index.html', context)
