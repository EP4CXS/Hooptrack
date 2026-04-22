"""
Django settings for development environment.

Overrides base settings for local development.
"""

from .base import *

# Development-specific settings
DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ['*']

# Email backend for development (prints to console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS - allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True

# Disable password validation for development (optional)
# AUTH_PASSWORD_VALIDATORS = []

# Static and media files served by Django in development
STATICFILES_DIRS = [BASE_DIR / 'static']

# Debug toolbar (optional, uncomment to enable)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1']

# Django REST Framework - more permissive in development
REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}
