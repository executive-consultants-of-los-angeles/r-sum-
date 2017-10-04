# -*- coding: utf-8 -*-
"""Models for rsum home application."""
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from docx import Document
from docx.shared import Inches

import cv
import section
import subsection
import project
import projectitem
import entry
import entryitem
