from configurations import Configuration, values

from {{cookiecutter.module_name}}.settings.base import BaseConfiguration


class Production(BaseConfiguration):

    DEBUG = bool(os.environ.get('DEBUG', False))
    TEMPLATE_DEBUG = DEBUG

    # ------------
    # Static Media
    # ------------

    DEFAULT_FILE_STORAGE = '{{cookiecutter.module_name}}.core.storage.MediaS3BotoStorage'
    STATICFILES_STORAGE = '{{cookiecutter.module_name}}.core.storage.StaticS3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value('')
    AWS_SECRET_ACCESS_KEY = values.Value('')
    AWS_STORAGE_BUCKET_NAME = values.Value('{{cookiecutter.module_name}}')
    AWS_PRELOAD_METADATA = values.BooleanValue(True)
    AWS_REDUCED_REDUNDANCY = values.BooleanValue(True)
    AWS_QUERYSTRING_AUTH = values.BooleanValue(False)

    STATIC_URL = values.URLValue('https://{0}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME))
    MEDIA_URL = values.URLValue('https://{0}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME))

    # ----------
    # Deployment
    # ----------

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
