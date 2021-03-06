"""
Django settings for syfboyaca4gavantel project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = [('Julio Brito', 'jucebridu@gmail.com')]

MANAGERS = ADMINS

ALLOWED_HOSTS = [
    os.getenv('ALLOWED_HOSTS_1'),
    os.getenv('ALLOWED_HOSTS_2'),
    os.getenv('ALLOWED_HOSTS_3'),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'users.apps.UsersConfig',
    'hardware.apps.HardwareConfig',
    'sites.apps.SitesConfig',
    'meetings.apps.MeetingsConfig',
    # third
    'crispy_forms',
    'import_export',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'syfboyaca4gavantel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'syfboyaca4gavantel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': '5432',
        'HOST': os.getenv('DB_HOST'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL')

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = os.getenv('MEDIA_URL')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AUTH_PROFILE_MODULE = 'users.Profile'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

IMPORT_EXPORT_USE_TRANSACTIONS = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

DATA_UPLOAD_MAX_MEMORY_SIZE = None

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# SECURE_SSL_REDIRECT = True
#
# SESSION_COOKIE_SECURE = True
#
# CSRF_COOKIE_SECURE = True

GS_BUCKET_NAME = os.getenv('BUCKET_NAME')

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'syf-boyaca4g-avantel-a605e56d0178.json')
)

try:
    from local_settings import *
except ImportError:
    pass
