#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.conf import settings

from schema.cv import CV

from export.word import ExportDocument

import json
import socket

print(settings.CV_NAME)

if socket.gethostname() == 'jrsum':
    CV_OWNER = 'jess-hartwell'
    CV_TEMPLATE = 'jcv'
    CV_NAME = 'general'

if socket.gethostname() == 'mrsum':
    CV_OWNER = 'jess-hartwell'
    CV_TEMPLATE = 'jcv'
    CV_NAME = 'general'

if socket.gethostname() == 'arsum':
    CV_OWNER = 'alex-harris'
    CV_TEMPLATE = 'acv'
    CV_NAME = 'engineer'


def index(request):
    cv_instance = CV()

    cv_id = cv_instance.check_sections(name_of_owner=CV_OWNER, name_of_cv=CV_NAME)
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

def export_docx(request, cv_id='1'):
    stream = ExportDocument().export(cv_id)

    # Special thanks to: https://stackoverflow.com/a/24122313 

    length = stream.tell()
    stream.seek(0)
    response = HttpResponse(
        stream.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename={0}-cv.docx'.format(CV_OWNER)
    response['Content-Length'] = length

    return response 
