#!/usr/bin/env python
"""Module for managing django."""
import os
import sys
import socket

from django.core.management import execute_from_command_line

def main():
    """Run manage.py."""
    if socket.gethostname() == 'ecla.solutions':
        settings = "rsum.settings"
    else:
        settings = "rsum.settings.{}".format(socket.gethostname())

    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
        execute_from_command_line(sys.argv)

main()
