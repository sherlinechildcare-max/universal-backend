import os
from pathlib import Path
from decouple import config, Csv
from datetime import timedelta

# ===============================
# Build paths inside the project
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# Security settings
# ===============================
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = [
    "carefor-seniors.com",
    "www.carefor-seniors.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://carefor-seniors.com",
    "https://www.carefor-seniors.com",
]

# ===============================
# Installed apps
# ===============================
INSTALLED_APPS = [
    # Django default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third‑party apps
    "rest_framework",
    "corsheaders",
    "axes",

    # Your project apps
    "users",
    "caregivers",
    "clients",
    "jobs",
    "chat",
    "payments",
    "reviews",
]

# ===============================
# Middleware
# ===============================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "axes.middleware.AxesMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ===============================
# Root URLs
# ===============================
ROOT_URLCONF = "config.urls"

# ===============================
# Templates
# ===============================
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

# ===============================
# WSGI
# ===============================
WSGI_APPLICATION = "config.wsgi.application"

# ===============================
# Database
# ===============================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
    }
}

# ===============================
# Password validation
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ===============================
# Internationalization
# ===============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ===============================
# Static files
# ===============================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ===============================
# Primary key type
# ===============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ===============================
# CORS Settings
# ===============================
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = config(
        "CORS_ALLOWED_ORIGINS",
        cast=Csv(),  # This handles the comma-separated values automatically
        default="https://carefor-seniors.com,https://www.carefor-seniors.com"
    )

# ===============================
# REST Framework
# ===============================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# ===============================
# JWT Authentication
# ===============================
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# ===============================
# Custom User Model
# ===============================
AUTH_USER_MODEL = "users.CustomUser"

# ===============================
# Security Hardening
# ===============================
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
X_FRAME_OPTIONS = "DENY"

# ===============================
# Axes Configuration
# ===============================
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # in hours
AXES_ONLY_USER_FAILURES = True