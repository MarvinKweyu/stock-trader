from __future__ import absolute_import, unicode_literals
import os
from dotenv import load_dotenv
from pathlib import Path

from stock_trader.config.base import *


load_dotenv()

DEBUG = True

SECRET_KEY = os.getenv("SECRET_KEY")


#  allow every access in local development
CORS_ALLOW_ALL_ORIGINS = True

BASE_DIR = Path(__file__).resolve().parent.parent
# use image db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


ALLOWED_HOSTS = ["*"]

# display mail on console
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
