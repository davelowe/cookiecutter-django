from configurations import Configuration, values

from {{cookiecutter.module_name}}.settings.base import BaseConfiguration


class Local(BaseConfiguration):
    DEBUG = True

    # INSTALLED_APPS = BaseConfiguration.INSTALLED_APPS + (
    #     'debug_toolbar',
    # )

    # MIDDLEWARE_CLASSES = BaseConfiguration.MIDDLEWARE_CLASSES + (
    #     'debug_toolbar.middleware.DebugToolbarMiddleware',
    # )

    # DEBUG_TOOLBAR_CONFIG = {
    #     'INTERCEPT_REDIRECTS': False,
    # }
