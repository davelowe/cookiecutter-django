#!/usr/bin/env python
import os
import sys


def parse_dotenv(dotenv):
    for line in open(dotenv):
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        v = v.strip("'").strip('"')
        yield k, v


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    # Look for a .dotenv in the same directory as the manage.py, and load it
    dotenv = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv):
        for k, v in parse_dotenv(dotenv):
            os.environ.setdefault(k, v)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.module_name}}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

    execute_from_command_line(sys.argv)
