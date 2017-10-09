from common import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mrsum', 
        'USER': 'psql',
        'PASSWORD': '',
        'HOST': 'apsql', 
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


OWNER = 'mrsum'
FILE = '/srv/rsum/cvs/jess/general.yml'
DIR = 'jess'

STATIC_URL = '/static/mrsum/'
STATIC_ROOT = '/srv/mrsum/rsum/static/mrsum'
