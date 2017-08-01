#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models
from home.schema.entryitem import EntryItem

sections_list = [
    'intro',
    'summary',
    'skills',
    'values',
    'experience',
    'education',
    'contact',
]


