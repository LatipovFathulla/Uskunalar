from pathlib import Path

from decouple import config
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'rest_framework',
    'parler',
    'adminsortable2',
    'widget_tweaks',
    'embed_video',
    'bs4',
    'active_link',
    'watermarker',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.humanize',
    'debug_toolbar',
    'corsheaders',

    'home',
    'about',
    'blog',
    'works',
    'videos',
    'lines',
    'biznes',
    'gallery',
    'clients',
]
JAZZMIN_SETTINGS = {
                    "site_title": "Uskunalar.uz", "site_header": "Uskunalar.uz", "site_brand": "Uskunalar.uz",
                    "site_logo": "images/favicon-us.png", "login_logo": None, "login_logo_dark": None,
                    "site_icon": None, "welcome_sign": "Uskunalar.uz", "copyright": "Uskunalar.uz", "user_avatar": None,
                    "show_ui_builder": True, "topmenu_links": [

                    # Url that gets reversed (Permissions can be added)
                    {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

                    # external url that opens in a new window (Permissions can be added)
                    {"name": "Products", "url": "/admin/home/bannerinfomodel/"},
                    {"name": "Categories", "url": "/admin/home/categorymodel/"},
                    {"name": "Subcategories", "url": "/admin/home/subcategorymodel/"},
                    {"name": "Lines", "url": "/admin/lines/linemodel/"},
                    {"name": "Blogs", "url": "/admin/blog/blogmodel/"},
                    {"name": "Biznes", "url": "/admin/blog/blogmodel/"},

                ], "usermenu_links": [
                    {"model": "auth.user"}
                ], "show_sidebar": True, "navigation_expanded": True, "hide_apps": [], "hide_models": [],
                    "order_with_respect_to": ["home", "about", "lines", "blog", "works"],
                    "related_modal_active": False, "custom_css": None, "custom_js": None,
                    "changeform_format": "horizontal_tabs",
                    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"}
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uskunalar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processor.home_categories',
                'home.context_processor.product_categories',
                'about.context_processor.index_categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'uskunalar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': BASE_DIR / 'uskunalar_cache',
#     }
# }
# cache
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


LANGUAGE_CODE = 'uz'

LANGUAGES = (
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
    ('en', _('English')),

)

MODELTRANSLATION_AUTO_POPULATE = True

PARLER_DEFAULT_LANGUAGE_CODE = 'uz'

PARLER_LANGUAGES = {
    None: (
        {'code': 'uz',},
        {'code': 'en',},
        {'code': 'ru',},
    ),
    'default': {
        'fallback': 'uz',             # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

LOCALE_PATHS = BASE_DIR / 'locale',

TIME_ZONE = 'Asia/Tashkent'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = BASE_DIR / 'assets',

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

WATERMARK_QUALITY = 95
WATERMARK_OBSCURE_ORIGINAL = True
WATERMARK_RANDOM_POSITION_ONCE = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RESULTS_CACHE_SIZE': 100,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 2000,   # milliseconds
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 9
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
#
# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000'
# )
try:
    from .settings_local import *
except ImportError:
    pass
