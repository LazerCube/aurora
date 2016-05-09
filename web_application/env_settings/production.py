from web_application.settings import *

DEBUG = False

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '0WUX5AwY6x',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '178.62.1.158']
STATIC_URL = '/static/'
