from common import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xander', 
        'USER': 'psql',
        'PASSWORD': '',
        'HOST': 'psql', 
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


FILE = '/srv/rsum/cvs/xander/general.yml'
OWNER = 'xander-harris'
DIR = 'xander'

STATIC_URL = '/static/xander/'
STATIC_ROOT = '/srv/rsum/xander/static/xander/'
