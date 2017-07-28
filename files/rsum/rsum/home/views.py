#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import CV

# Create your views here.

def index(request):

    cv = CV()
    cv.check_sections()

    return render(request, 'home/index.html', {})
