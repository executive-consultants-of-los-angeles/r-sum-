#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render

from .models import CV

# Create your views here.

def index(request):

    cv = CV()
    print(cv.objects.all())
    cv.check_sections()

    return render(request, 'home/index.html', {})
