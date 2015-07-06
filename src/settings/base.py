import os, re
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
makepath = lambda *f: os.path.join(BASE_DIR, *f)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2x-r4x+4oxdmvvxenj*dhq##uxrgl%f3=#+l*1s32y=f^51hz'

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Oslo'

# Application definition
INSTALLED_APPS = (
    'grappelli',
    
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'app.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.core.context_processors.request',
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.static',
   'django.contrib.messages.context_processors.messages'
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

LANGUAGE_CODE = 'en-gb'
STANDARD_USER_LANGUAGE = 'en-gb'
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'H.i'

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False
USE_I18N = True
USE_L10N = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MEDIA_ROOT = makepath("media")
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    makepath("static"),
)

# Used by collect static and nginx
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

GRAPPELLI_ADMIN_TITLE = "Eirik M Hammerstad - Blog" 

## Translates messages tags into our correct CSS classes
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-debug',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-info',
    messages.ERROR: 'alert-error',
}

SITE_ID = 1

# Login specific
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = "/logout/"