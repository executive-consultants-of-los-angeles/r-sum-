#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models

from schema.cv import CV 

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

    print(json.dumps(context.get('cv')[1],indent=1))

    return render(request, 'home/index.html', context)
