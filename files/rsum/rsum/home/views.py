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

    cv = cv_i.check_sections()
    print(json.dumps(cv,indent = 1))
    
    context = {}

    return render(request, 'home/index.html', context)
