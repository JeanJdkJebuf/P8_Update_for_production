from . import *

SECRET_KEY = os.environ.get("KEY_PROD")

DEBUG = False

ALLOWED_HOSTS = ["51.210.13.67"]

DB_NAME = os.environ.get("BDD")
DB_USER = os.environ.get("USER")
DB_PW = os.environ.get("PW_POSTGRES")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PW,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

