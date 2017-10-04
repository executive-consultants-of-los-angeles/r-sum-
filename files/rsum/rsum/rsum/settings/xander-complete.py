from common import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xander-complete', 
        'USER': 'psql',
        'PASSWORD': '',
        'HOST': 'psql', 
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


OWNER = 'xander-harris'
CV = 'complete'
DIR = 'xander'

STATIC_URL = '/static/{}/'.format(OWNER)
STATIC_ROOT = '/srv/{}/static/{}/'.format(OWNER, OWNER)
