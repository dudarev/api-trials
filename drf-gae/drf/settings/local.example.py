from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'drf',
        'USER': '<your-database-user>',
        'PASSWORD': '<your-database-password>',
    }
}
