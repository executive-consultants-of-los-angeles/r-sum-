#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render

import models

# Create your views here.

def index(request):

    print(models.ProjectListItem.objects.values_list())
    cv_i = models.CV()
    cv_i.check_sections()
    print(models.CV.objects.values_list())

    pli = models.ProjectListItem.objects.values_list()
    print(pli)

    return render(request, 'home/index.html', {})
