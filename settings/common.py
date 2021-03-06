# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

ADMINS = (
    ("David Barragán", "davi.barragan@kaleidos.net"),
    ("Xavier Julián", "xavier.julian@kaleidos.net"),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "e_tbs-l(@so@u(go#qouuhtkh656%a=erx%bb(pi=hl2j=z%yl"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "cinemair",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"


# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "cinemair",
    "cinemair.common",
    "cinemair.users",
    "cinemair.movies",
    "cinemair.cinemas",
    "cinemair.shows",
    "cinemair.favorites",
)


AUTH_USER_MODEL = "users.User"


MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    'cinemair.common.middleware.cors.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

ROOT_URLCONF = "cinemair.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"


# Rest framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # Mainly used by taiga-front
        "cinemair.users.backends.Token",

        # Mainly used for api debug.
        "cinemair.users.backends.Session",
    ),
}


# The MovieDB API KEY
THEMOVIEDB_API_KEY = "247e0e9d8f8cadd19b1cc9b925a68270"
THEMOVIEDB_LANG_CODE = "es" # None == 'en', 'es', 'de', 'fr'....


# Google Auth
GOOGLE_API_CLIENT_ID = "661976506904-t5hdjfsvggji8vt9k2jqfk1bs2st3c23.apps.googleusercontent.com"
GOOGLE_API_CLIENT_SECRET = "midz4fIPfiqNIcCz6brwYTya"
GOOGLE_API_REDIRECT_URI = "http://localhost:8100/"
