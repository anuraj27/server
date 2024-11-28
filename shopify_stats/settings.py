import json
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CLIENT_SECRET_PATH = os.path.join(BASE_DIR, 'shopify_stats', 'client_secret1.json')
# Load the client secrets from the JSON file
with open(CLIENT_SECRET_PATH, 'r') as file:
    client_secret_data = json.load(file)
    

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stats',
    'users',
    'django_celery_beat',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
]
SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'shopify_stats.urls'

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
            ],
        },
    },
]


WSGI_APPLICATION = 'shopify_stats.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SHOPIFY_API_KEY = 'your_shopify_api_key'
SHOPIFY_PASSWORD = 'your_shopify_password'
SHOPIFY_STORE_URL = 'your_shopify_store.myshopify.com'

BIGQUERY_DATASET_ID = 'your_dataset_id'
BIGQUERY_TABLE_ID = 'your_table_id'

CELERY_BROKER_URL = 'redis://localhost:6379/0'



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'allauth.account.auth_backends.AuthenticationBackend',  # For Django Allauth
]


LOGIN_REDIRECT = "/"
LOGOUT_REDIRECT = "/"

BASE_APP_URL = "http://localhost:3000"
BASE_API_URL = "http://localhost:8000"

# Extract the necessary fields from the JSON data
CLIENT_ID = client_secret_data['web']['client_id']
CLIENT_SECRET = client_secret_data['web']['client_secret']
REDIRECT_URI = client_secret_data['web']['redirect_uris'][0]  # Assuming only one URI is present
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

# OAuth Config Dictionary
OAUTH_CONFIG = {
    'web': {
        'client_id': CLIENT_ID,
        'project_id': client_secret_data['web']['project_id'],
        'auth_uri': client_secret_data['web']['auth_uri'],
        'token_uri': client_secret_data['web']['token_uri'],
        'auth_provider_x509_cert_url': client_secret_data['web']['auth_provider_x509_cert_url'],
        'client_secret': CLIENT_SECRET,
        'redirect_uris': client_secret_data['web']['redirect_uris'],
        'javascript_origins': client_secret_data['web']['javascript_origins'],
    }
}



ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': CLIENT_ID,
            'secret': CLIENT_SECRET,
            'key': ''
        }
    }
}
