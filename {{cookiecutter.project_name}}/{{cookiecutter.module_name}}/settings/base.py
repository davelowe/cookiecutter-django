import os
import sys

import dj_database_url
from configurations import Configuration, values

import {{cookiecutter.module_name}}


class BaseConfiguration(Configuration):

    # -------
    # General
    # -------

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)

    ADMINS = (
        ('{{cookiecutter.author}}', '{{cookiecutter.email}}'),
    )

    MANAGERS = ADMINS

    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = values.ListValue(['localhost:8000'])

    INTERNAL_IPS = ('127.0.0.1',)

    # Local time zone for this installation. Choices can be found here:
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # although not all choices may be available on all operating systems.
    # In a Windows environment this must be set to your system time zone.
    TIME_ZONE = 'America/Chicago'

    # Language code for this installation. All choices can be found here:
    # http://www.i18nguy.com/unicode/language-identifiers.html
    LANGUAGE_CODE = 'en-us'

    SITE_ID = 1

    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False

    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale.
    USE_L10N = True

    # If you set this to False, Django will not use timezone-aware datetimes.
    USE_TZ = True

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'CHANGEME!!!'

    # List of callables that know how to import templates from various sources.
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.debug',
    )

    ROOT_URLCONF = values.Value('{{cookiecutter.module_name}}.urls')

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = '{{cookiecutter.module_name}}.wsgi.application'

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.flatpages',
        'django.contrib.admin',
        '{{cookiecutter.module_name}}.core',
    )


    # --------
    # Database
    # --------

    DATABASES = {"default": dj_database_url.config()}


    # -----
    # Paths
    # -----

    PROJECT_MODULE_PATH = os.path.dirname(os.path.realpath({{cookiecutter.module_name}}.__file__))
    PROJECT_PATH, PROJECT_MODULE_NAME = os.path.split(PROJECT_MODULE_PATH)

    PYTHON_BIN = os.path.dirname(sys.executable)
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')

    STATIC_ROOT = values.PathValue(os.path.join(VAR_ROOT, 'static'),
                                   checks_exists=False)
    MEDIA_ROOT = values.PathValue(os.path.join(VAR_ROOT, 'media'),
                                  checks_exists=False)
    STATICFILES_DIRS = (os.path.join(PROJECT_MODULE_PATH, 'static'),)
    TEMPLATE_DIRS = (os.path.join(PROJECT_MODULE_PATH, 'templates'),)

    for path in (VAR_ROOT, STATIC_ROOT, MEDIA_ROOT):
        if not os.path.exists(path):
            os.mkdir(path)


    # -----
    # Media
    # -----

    STATIC_URL = values.Value('/static/')
    MEDIA_URL = values.Value('/media/')


    # -------
    # Logging
    # -------

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
