
import os
from config.env import BASE_DIR, env
from config.settings.all_auth import *

# Read environment variables from .env file
env.read_env(os.path.join(BASE_DIR, '.env'))
# Base settings
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG',default=False)



ALLOWED_HOSTS = []
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Application definition

DJANGO_APPS = [
    "unfold",  # before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.forms',  
]

THIRD_PARTY_APPS = [
    # 3rd party libraries
    'compressor', # to be used with tailwind css 
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
    'formtools',
    'phonenumber_field',
] + ALL_AUTH_APPS

LOCAL_OWN_APPS =[
        # Custom apps
    'users.apps.UsersConfig',
    'payments.apps.PaymentsConfig',
    'products.apps.ProductsConfig',
    'core.apps.CoreConfig',
    'django_htmx.apps.DjangoHtmxConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_OWN_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ALL_AUTH_MIDDLEWARE,
    
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',                 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders': [
            #     "django.template.loaders.filesystem.Loader",
            #     "django.template.loaders.app_directories.Loader",
            # ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # To get access to CLIENT_ID in the context template
                "users.utils.context_processors.settings_context",
                "users.utils.context_processors.google_client_id",
                "users.utils.context_processors.google_maps_api_key", #GOOGLE_MAPS_API_KEY
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    ALL_AUTH_AUTHENTICATION_BACKENDS,
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
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

# SECURITY
SESSION_COOKIE_HTTPONLY = True      # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
CSRF_COOKIE_HTTPONLY = True         # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
SECURE_BROWSER_XSS_FILTER = True    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
X_FRAME_OPTIONS = "DENY"            # https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"


#PHONE NUMBER VALIDATION
PHONENUMBER_DEFAULT_REGION = 'FR'


# LOGIN_URL = 'account_login'
# LOGIN_REDIRECT_URL = 'users:redirect'


# Here is a good place to import all 3rd party settings
# from config.settings.celery import *
# from config.settings.file_storage import *
