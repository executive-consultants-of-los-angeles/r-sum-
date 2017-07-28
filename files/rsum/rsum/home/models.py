# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class CV(models.Model):
    section = models.CharField(maxlength=200)
