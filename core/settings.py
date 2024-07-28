import os
from dotenv import load_dotenv
from corsheaders.defaults import default_headers


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')

SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(os.getenv("DEBUG"))

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Register',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'base',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'requestlogs.middleware.RequestLogsMiddleware',
]

REQUESTLOGS = {
    'SECRETS': ['password', 'token'],
    'METHODS': ('GET', 'PUT', 'PATCH', 'POST', 'DELETE'),
}

REST_FRAMEWORK={
    'EXCEPTION_HANDLER': 'requestlogs.views.exception_handler',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'requestlogs_to_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        },
    },
    'loggers': {
        'requestlogs': {
            'handlers': ['requestlogs_to_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.teste',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
        # "ENGINE": "django.db.backends.postgresql",
        # "NAME": os.getenv("DATABASE_NAME"),
        # "USER": os.getenv("DATABASE_USER"),
        # "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        # "HOST": "127.0.0.1",
        # "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Forma de mandar emails no django com gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv("USER_EMAIL")
# EMAIL_HOST_PASSWORD = os.getenv("SENHA_EMAIL")

from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.DEBUG: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
}