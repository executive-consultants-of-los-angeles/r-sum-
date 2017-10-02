#!/usr/bin/env python

from common import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mrsum', 
        'USER': 'psql',
        'PASSWORD': '',
        'HOST': 'mpsql', 
        'PORT': 5432,
    }
}

