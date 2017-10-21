"""
Django settings for redirect project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os


# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = ''

ALLOWED_HOSTS = []


# Application definition.

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
)

SECURE_SSL_REDIRECT = True

ROOT_URLCONF = 'redirect.urls'

WSGI_APPLICATION = 'redirect.wsgi.application'


# Internationalization.
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Local settings. Allow any settings to be defined in local_settings.py, which
# should be ignored in your version control system, allowing for settings to be
# defined per machine. Instead of doing "from .local_settings import *", we use
# exec so that local_settings has full access to everything defined in this
# module.

PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))

f = os.path.join(PROJECT_APP_PATH, 'local_settings.py')
if os.path.exists(f):
    exec(open(f, 'rb').read())
