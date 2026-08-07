import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Render აყენებს RENDER environment variable-ს ყველა სერვისზე რასაც უშვებს,
# ასე იგებს აპლიკაცია ლოკალურად მუშაობს თუ production-ში.
IS_PRODUCTION = "RENDER" in os.environ

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-r$*%b=x&@3e%b#wj=*rx5i6mzb=&xi9sy8u5*o^9ejy^)%^0z0"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not IS_PRODUCTION

# დომენების სია, რომლებსაც აპლიკაცია პასუხობს
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local apps
    "pages",
    "accounts",
    "cars",
    # 3rd-party apps
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise ემსახურება CSS/სურათებს production-ში.
    # უნდა იყოს ზუსტად SecurityMiddleware-ის ქვემოთ.
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "carmarket.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "carmarket.wsgi.application"


# Database
# Render გვაძლევს DATABASE_URL-ს PostgreSQL-ისთვის.
# ლოკალურად (ეს ცვლადი არ არსებობს) ისევ SQLite გამოიყენება.
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# collectstatic აგროვებს ყველა static ფაილს ამ ფოლდერში,
# საიდანაც WhiteNoise მათ ემსახურება.
STATIC_ROOT = BASE_DIR / "staticfiles"

AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# დამატებითი production-only პარამეტრები.
# ლოკალურად ეს გამორთულია, თორემ https://127.0.0.1-ზე გადამისამართებას სცადებდა.
if IS_PRODUCTION:
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    # Render HTTPS-ს თავად ამუშავებს და plain HTTP-ს გადმოგვცემს,
    # ამიტომ Django-მ ეს header უნდა წაიკითხოს რომ იცოდეს რეალურად https-ზეა.
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True