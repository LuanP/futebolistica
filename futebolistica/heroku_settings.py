import dj_database_url
import os

from settings import *


DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ADMINS = ADMINS = (
    ('Luan Pablo', 'luanpab@gmail.com'),
)

MANAGERS = ADMINS

CWD = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = ['*', ]

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(CWD, 'static'),
)

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DATABASES['default'] = dj_database_url.config()
