"""
Django settings for photo project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n7&w3*@cdolm_d2&(tv6#yzil0wi7z8a1_+42v(+9wzooz#uzg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'ckeditor_uploader',
    'ckeditor',

    'photo',
    'emails.apps.EmailsConfig',
    'main.apps.MainConfig',
    'user.apps.UserConfig',
    'shop.apps.ShopConfig',
    'mathfilters',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.middleware.init_session',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'photo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'user.context_processor.link_login',
            ],

        },
    },
]

WSGI_APPLICATION = 'photo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'user.UserModel'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Omsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'pictures')

MEDIA_URL = '/pictures/'

# Email settings
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'kaverinstudio@ya.ru'
EMAIL_HOST_PASSWORD = 'vjzYfnfkb198'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

FROM_EMAIL = 'kaverinstudio@ya.ru'
FROM_ADMIN = 'kaverinstudio@gmail.com'

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'width': '1296px',
        'height': '500px',
    },
}

THUMBNAIL_ALIASES = {
    "": {
        "small": {"size": (150, 150)}
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'long': {
            'format': "%(asctime)s | %(levelname)8s | %(name)10s | %(filename)s.%(funcName)s:%(lineno)s - %(message)s",
        },
        'short': {
            'format': "%(asctime)s|%(levelname)s|%(name)s - %(message)s",
        },
    },
    'handlers': {
        'default': {
            'formatter': 'long',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'formatter': 'short',
            'class': 'logging.FileHandler',
            'filename': 'log.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.*': {
            'handlers': ['default', 'file'],
            'level': 'INFO',
        },
        'asyncio': {
            'level': 'WARNING'
        },
        'asyncio.*': {
            'level': 'WARNING'
        },
        'PIL.*': {
            'level': 'WARNING'
        },
    }}
