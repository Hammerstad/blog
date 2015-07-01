import os
from settings.base import INSTALLED_APPS, MIDDLEWARE_CLASSES, TEMPLATE_CONTEXT_PROCESSORS

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#To show debug toolbar or not. Only shows on debug == True
def custom_show_toolbar(request):
    return DEBUG

INSTALLED_APPS += (
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'INTERCEPT_REDIRECTS': False,  # Set to True if you want to see requests before you are redirected
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + '/project.db'
    }
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
   'django.core.context_processors.debug',
)