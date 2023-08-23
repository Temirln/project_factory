from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": "1kNHx4EMtV8iUSzAqX1k",
        "HOST": "containers-us-west-208.railway.app",
        "PORT": "7137",
    }
}

ALLOWED_HOSTS = [".vercel.app"]

WSGI_APPLICATION = "project_factory.wsgi_prod.application"

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'info_file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'prod_logs/info.log'
#         },
#         'debug_file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'prod_logs/debug.log'
#         },
#         'error_file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'prod_logs/error.log'
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['debug_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         '': {
#             'handlers': ['error_file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'project_api': {
#             'handlers': ['info_file'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     },
# }
