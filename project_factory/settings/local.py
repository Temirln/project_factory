from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ["*"]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'info_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'local_logs/info.log'
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'local_logs/debug.log'
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'local_logs/error.log'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'project_api': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': True,
        }
    },
}