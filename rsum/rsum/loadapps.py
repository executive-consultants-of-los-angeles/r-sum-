"""Module creates database entries for a profile."""
import django
from django.conf import settings


def main():
    try:
        settings.configure()
    except RuntimeError:
        pass
    return django.setup()


main()
