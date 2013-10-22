from {{cookiecutter.module_name}}.settings.base import *


DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG


# ------------
# Static Media
# ------------

DEFAULT_FILE_STORAGE = 'checkoff.core.storage.MediaS3BotoStorage'
STATICFILES_STORAGE = 'checkoff.core.storage.StaticS3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_PRELOAD_METADATA = True
AWS_REDUCED_REDUNDANCY = True
AWS_QUERYSTRING_AUTH = False

STATIC_URL = 'https://s3.amazonaws.com/{}/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_URL = 'https://s3.amazonaws.com/{}/media/'.format(AWS_STORAGE_BUCKET_NAME)

# ----------
# Deployment
# ----------

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
