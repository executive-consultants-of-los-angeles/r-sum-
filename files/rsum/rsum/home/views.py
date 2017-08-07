#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models

from schema.cv import CV

import json


def index(request):
    cv_instance = CV()

    cv_id = cv_instance.check_sections(name_of_owner='alex', name_of_cv='complete')
    cv = cv_instance.get_cv(cv_id=cv_id)

    context = {
        'cv': cv.get('sections') 
    }

    skills = cv_instance.get_skills(context)
    context.get('cv')[2].update({
        'skills': skills,
    })

    values = cv_instance.get_values(context) 
    context.get('cv')[3].get('content')[1].update({
        'content': values
    })

    experience = cv_instance.get_experience(context) 
    context.get('cv')[4].update({
        'experience': experience
    })

    education = context.get(
        'cv'
    )[5].get('content')[3].get('content')[0]
    projects = education.get(
        'content'
    ).replace("'", '').replace("[", '').replace("]", '').split(", ")
    context.get('cv')[5].update({
        'projects': projects
    })

    return render(request, 'home/index.html', context)
