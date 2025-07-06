"""
production settings, refer to mysite.settings.development for development settings; they both extend the base.py settings, which contain common settings. 
"""

from .base import *
import os, secrets

""" major variables are declared here for readability
and easy maintenance
"""

web_host = 'reportsalchemy.pythonanywhere.com'

# SECRET KEY GENERATION
SECRET_KEY = os.getenv('SECRET_KEY')
if SECRET_KEY == None:
    os.environ["SECRET_KEY"] = secrets.token_urlsafe(32)
    SECRET_KEY = os.getenv('SECRET_KEY')
 

DEBUG = False

ALLOWED_HOSTS = [web_host]


CSRF_TRUSTED_ORIGINS=[
        'http://' + web_host,
        'https://' + web_host,

        ]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
        'default':{
            'ENGINE':'django.db.backends.sqlite3',
            'NAME':'/home/reportsalchemy/ERP-website-template/db.sqlite3'
            },
    'main_default': {    
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PGDATABASE'),
        'USER':  os.getenv('PGUSER'),
        'PASSWORD': os.getenv('PGPASSWORD'),
        'HOST': os.getenv('PGHOST'),
        'PORT': os.getenv('PGPORT'),

                'TEST':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':'testdatabase.db',
        }
                }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '../static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAILING SETTINGS

EMAIL_HOST_USER = "granzularcodex@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 60 * 2
