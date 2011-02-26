# Django settings for django_twitter project.
import os

SETTINGS_DIR = os.path.split(__file__)[0]
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Add the following information in application settings
ADMINS = (
    # ('Name', 'Email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SETTINGS_DIR, "database.sqlite"),
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Denver'

# ENTER SECRET KEY IN APPLICATION SETTINGS!
SECRET_KEY = ''

from application_settings import *

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(SETTINGS_DIR, 'static', '')

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'twit.util.middleware.TwitterAPIMiddleware',
)

ROOT_URLCONF = 'twit.urls'

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'twit.analysis',
    'twit.accounts',
    'twit.api',
    'south',
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

try:
    # Not required
    from local_settings import *
except ImportError:
    pass