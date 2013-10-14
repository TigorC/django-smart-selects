#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from django.conf import settings
from django.core.management import call_command

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

settings.configure(
    INSTALLED_APPS=('smart_selects', 'smart_selects_tests'),
    ROOT_URLCONF='smart_selects_tests.urls',
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:',
        }
    }
)

if __name__ == "__main__":
    call_command('test', 'smart_selects_tests')
