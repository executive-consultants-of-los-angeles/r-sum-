"""Module creates database entries for a profile."""
import django
import dj_database_url
from django.conf import settings

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


def main():
    try:
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
        settings.configure(DATABASES=DATABASES)
    except RuntimeError:
        pass
    return django.setup()


main()
