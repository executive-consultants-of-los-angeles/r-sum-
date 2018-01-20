"""Django settings for rsum project."""
# pylint: disable=missing-docstring
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's7g+(@&fc-iycjd=yk)%t$_3@h3gx(!v$c9fh1pbj@zi6r6a(6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.gahan-corporation.com',
    '[::]',
    '.herokuapp.com',
    'rsum',
]


# Application definition

INSTALLED_APPS = [
    'rsum',
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OWNER = 'xander'
DIR = 'xander'
FILE = '/srv/static/profiles/xander/complete.yml'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rsum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rsum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xander',
        'USER': 'xander',
        'PASSWORD': '',
        'HOST': 'pg.gc',
        'PORT': '5432',
    }
}

DATABASE_ENV = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(DATABASE_ENV)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': (
        "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator")},
    {'NAME': (
        "django.contrib.auth.password_validation."
        "MinimumLengthValidatorr")},
    {'NAME': (
        "django.contrib.auth.password_validation."
        "CommonPasswordValidator")},
    {'NAME': (
        "django.contrib.auth.password_validation."
        "NumericPasswordValidator")},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = False
USE_L10N = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'static/',
]
