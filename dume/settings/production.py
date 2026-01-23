"""
Production settings for dume project.
Testing environment - relaxed security settings.
"""

from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-test-key-change-in-production')
if not SECRET_KEY or SECRET_KEY == 'django-insecure-test-key-change-in-production':
    import secrets
    SECRET_KEY = secrets.token_urlsafe(50)

# SECURITY WARNING: don't run with debug turned on in production!
# Testing environment - allow debug
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Allow all hosts for testing environment (including internal Fly.io IPs for health checks)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
if '*' in ALLOWED_HOSTS:
    ALLOWED_HOSTS = ['*']

# Security settings for production - relaxed for testing
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'False') == 'True'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'  # Relaxed for testing

# Static files in production - use whitenoise (simplified for testing)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


