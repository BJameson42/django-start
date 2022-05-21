import os
from pathlib import Path

# System
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = int(os.environ.get("DEBUG", default=0))
LANGUAGE_CODE = "en-us"
ROOT_URLCONF = "config.urls"
SECRET_KEY = os.environ.get("SECRET_KEY")
TIME_ZONE = "US/Eastern"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "config.wsgi.application"

# Email Configuration
ADMINS = [("Admin", e) for e in os.environ.get("EMAIL_ADMINS").split(" ")]
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
EMAIL_USE_TLS = int(os.environ.get("EMAIL_USE_TLS"))

# Database Connection
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# Static Files
STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "site/static")]

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Authentication
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = ["config.hasher.MyBcryptHasher"]
