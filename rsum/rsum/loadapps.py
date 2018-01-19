"""Module creates database entries for a profile."""
import django
from django.conf import settings


def main():
    settings.configure()
    return django.setup()


main()
