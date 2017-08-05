#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models

from schema.cv import CV

import json


def index(request):
    cv_i = CV()

    cv_check_sections = cv_i.check_sections()
    cv = cv_i.get_cv()

    sections = cv_i.sort_sections(cv) 

    context = {
        'cv': sections
    }

    skills = cv_i.get_skills(context)

    context.get('cv')[2].update({
        'skills': skills,
    })

    values = cv_i.get_values(context) 
    context.get('cv')[3].get('values').get('content')[1].update({
        'content': values
    })

    experience = cv_i.get_experience(context) 
    context.get('cv')[4].get('experience').update({
        'experience': experience
    })

    education = context.get(
        'cv'
    )[5].get('education').get('content')[3].get('content')[0]
    projects = education.get(
        'content'
    ).replace("'", '').replace("[", '').replace("]", '').split(", ")
    context.get('cv')[5].get('education').update({
        'projects': projects
    })

    return render(request, 'home/index.html', context)
