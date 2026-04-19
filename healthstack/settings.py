from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Environment variables ─────────────────────────────────────────────
env = environ.Env(
    DEBUG=(bool, False),
)
# Gracefully skip if .env doesn't exist (e.g. on Render where env vars are set directly)
env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# ── Security ──────────────────────────────────────────────────────────
# Fix: was hardcoded plaintext secret key in source code
SECRET_KEY = env('SECRET_KEY', default='change-me-in-production')

# Fix: was hardcoded True — always exposes errors and debug info in production
DEBUG = env('DEBUG', default=False)

# Fix: was hardcoded local IPs only — breaks on any other machine/server
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# ── Installed Apps ─────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital.apps.HospitalConfig',
    'hospital_admin.apps.HospitalAdminConfig',
    'doctor.apps.DoctorConfig',
    'pharmacy.apps.PharmacyConfig',
    'sslcommerz.apps.SslcommerzConfig',
    'widget_tweaks',
    'rest_framework',
    'ChatApp.apps.ChatappConfig',
]

# Only enable debug toolbar locally — do not load it in production
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

# ── Middleware ─────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Fix: whitenoise was in requirements but never added to middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'healthstack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'healthstack.wsgi.application'

# ── Database ───────────────────────────────────────────────────────────
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600,
    )
}

# ── Password Validation ────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalisation ───────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ── Static & Media ─────────────────────────────────────────────────────
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# In DEBUG: use simple storage (avoids .map file errors from third-party JS)
# In production: use WhiteNoise compressed storage for efficiency
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files are stored inside the static directory so WhiteNoise can serve
# them in production (Render) without a separate media server.
# MEDIA_URL must match STATIC_URL prefix so collectstatic puts them where
# WhiteNoise already serves: /static/images/...
MEDIA_URL = '/static/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# ── SSLCommerz ─────────────────────────────────────────────────────────
# Fix: credentials were hardcoded as "#" — now read from environment
STORE_ID = env('SSLCOMMERZ_STORE_ID', default='')
STORE_PASSWORD = env('SSLCOMMERZ_STORE_PASSWORD', default='')
STORE_NAME = 'MediCare'

# ── Email ──────────────────────────────────────────────────────────────
# Fix: credentials were hardcoded as "#" — now read from environment
EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER or 'noreply@medicare.com')

# ── Auth ───────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'hospital.User'

# SESSION: 45 minutes
SESSION_COOKIE_AGE = 45 * 60
SESSION_SAVE_EVERY_REQUEST = True

# ── Security Headers (production only) ────────────────────────────────
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True