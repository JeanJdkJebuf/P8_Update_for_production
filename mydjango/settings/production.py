from . import *

SECRET_KEY ="AQng7sNIlv7vOBObGU18D5z3" 

DEBUG = False

ALLOWED_HOSTS = ["51.210.13.67"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sitebeurre',
        'USER': 'jean',
        'PASSWORD': 'g5E4e3gr9A2ddz56rt12er',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

