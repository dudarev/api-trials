from .base import *


ALLOWED_HOSTS = ['<your-app.appspot.com>']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '/cloudsql/<your-cloudsql-connection string>',
        'NAME': 'drf',
        'USER': '<your-database-user>',
        'PASSWORD': '<your-database-password>',
    }
}
