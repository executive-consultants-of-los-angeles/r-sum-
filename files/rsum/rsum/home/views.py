#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render
from django.db import models

import json

# Create your views here.

def index(request):
    context = {}

    return render(request, 'home/index.html', context)
