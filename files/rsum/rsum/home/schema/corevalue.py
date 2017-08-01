#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models

class CoreValue(models.Model):
    section = models.ForeignKey('home.Section', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    content = models.CharField(max_length=200, null=True)

    class Meta:
        app_label = 'home'
        managed = True
