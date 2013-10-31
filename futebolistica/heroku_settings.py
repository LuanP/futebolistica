import dj_database_url
import os

from settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ADMINS = (
    ('Luan Pablo', 'luanpab@gmail.com'),
)

MANAGERS = ADMINS

CWD = os.path.abspath(os.path.dirname(__file__))

STATIC_URL = 'http://futebolistica.herokuapp.com/static/'

ALLOWED_HOSTS = ['*', ]

STATIC_ROOT = os.path.join(CWD, 'static')

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DATABASES['default'] = dj_database_url.config()
