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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


OWNER = 'mrsum'
FILE = 'general'
DIR = 'jess'

STATIC_URL = '/static/{}/'.format(OWNER)
STATIC_ROOT = '/srv/{}/static/{}/'.format(OWNER, OWNER)
