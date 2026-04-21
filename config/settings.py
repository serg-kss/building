from pathlib import Path
from dotenv import load_dotenv
import os
from django.utils.translation import gettext_lazy as _

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "django-insecure-5t!2b)6snrkmq@%#*4#et5*8$xyvj5ys)q=i4*#dt)f8@9od*+"

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'seo',
    'main.apps.MainConfig',
    'services',
    'portfolio',

    "tinymce",
    "cookie_consent",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates',],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                "main.context_processors.site_settings",
                "django.template.context_processors.request"
            ],
        },
    },
]

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "seo.context_processors.seo"
]

WSGI_APPLICATION = "config.wsgi.application"



# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = "Europe/Kyiv"

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = "/media/"

if DEBUG:
    MEDIA_ROOT = BASE_DIR / "media"
else:
    MEDIA_ROOT = "/var/data/media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


JAZZMIN_SETTINGS = {

    "site_title": "БІЛДІНГ ЕСТЕЙТ Admin",
    "site_header": "Building CMS",
    "site_brand": "БІЛДІНГ ЕСТЕЙТ",
    "custom_css": "assets/css/admin.css",

    "welcome_sign": "Керування сайтом",

    "site_logo": None,
    "login_logo": None,
    "site_icon": "assets/img/favicons/favicon-32x32.png",
    "login_logo": "assets/img/logo-admin.png",


    "show_sidebar": True,
    "show_ui_builder": False,
    "navigation_expanded": True,

    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": [
        
        "main",
        "services",
        "portfolio",
        "seo",
    ],

    "icons": {

        "auth.user": "fas fa-user",

        "main.HomePage": "fas fa-home",
        "main.AboutPage": "fas fa-building",
        "main.ContactMessages": "fas fa-envelope",
        "main.SocialMedia": "fas fa-share-alt",

        "services.Service": "fas fa-tools",

        "portfolio.Portfolio": "fas fa-images",

        "seo.PageSEO": "fas fa-search",
    },

    "topmenu_links": [

        {"name": "Сайт", "url": "/", "new_window": True},

        {"model": "main.HomePage"},
        {"model": "main.AboutPage"},

    ],

    "usermenu_links": [
        {"name": "Перейти на сайт", "url": "/", "new_window": True},
    ],

    "hide_apps": [
        "auth",
    ],
    

}

JAZZMIN_UI_TWEAKS = {

    "theme": "flatly",

    "navbar_small_text": False,
    "sidebar_small_text": False,

    "brand_small_text": False,

    "accent": "accent-primary",

    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,

    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "footer_fixed": False,

}

TINYMCE_DEFAULT_CONFIG = {

    "height": 500,
    "width": "auto",
    "menubar": True,

    "license_key": "gpl",

    "skin": "oxide-dark",
    "content_css": "dark",

    "plugins": """
        advlist autolink lists link image charmap preview anchor
        searchreplace visualblocks code fullscreen
        insertdatetime media table help wordcount
    """,

    "toolbar": """
        undo redo | blocks |
        bold italic underline |
        alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent |
        link image media table |
        removeformat | code fullscreen
    """,

    "toolbar_mode": "sliding",

    "image_caption": True,
    "image_advtab": True,

    "automatic_uploads": True,

    "file_picker_types": "image",

    "mobile": {
        "toolbar_mode": "scrolling"
    },

    "content_style": """
        body {
            background-color: #212529;
            color: #f8f9fa;
            font-size: 16px;
        }

        p, h1, h2, h3, h4, h5, h6 {
            color: #f8f9fa;
        }

        a {
            color: #4dabf7;
        }
    """,
}
TINYMCE_DEFAULT_CONFIG["image_dimensions"] = False
TINYMCE_DEFAULT_CONFIG["image_class_list"] = [
    {"title": "Responsive", "value": "img-fluid"},
]