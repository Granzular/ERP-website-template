from .base import *
import os
import socket

SECRET_KEY = 'django-insecure-2&%bk7+w-=hkwagbn&(19e@009&+(ny%_lj@!_x^ydl212ism#'

DEBUG = True

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = '127.0.0.1'
port = 8000
try:
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
except:
    pass
ALLOWED_HOSTS = [ip,'localhost']


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            }
        }


