from settings import INSTALLED_APPS


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_futebolistica.db',
    }
}

SECRET_KEY = 'hertyhtyu47686*&46735YH#%356#%36#2#$%1#$$%34(*&()7htRHrt'

try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'django_extensions',
    )
