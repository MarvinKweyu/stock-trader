from __future__ import absolute_import, unicode_literals

import os

import dj_database_url
import dotenv

from stock_trader.settings.base import *

env = os.environ.copy()


DEBUG = False


SECRET_KEY = os.getenv("SECRET_KEY")


ALLOWED_HOSTS = ["my_domain"]


DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "SQL_ENGINE", "django.db.backends.postgresql_psycopg2"
        ),
        "NAME": os.environ.get("SQL_DATABASE", "stocktrader"),
        "USER": os.environ.get("SQL_USER", "retailer"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "retailer"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", ""),
    }
}


#  once frontend is up
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]


# gmail while domain account is set up
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
