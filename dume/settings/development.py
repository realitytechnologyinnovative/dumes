"""
Development settings for dume project.
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-change-this-in-production-!@#$%^&*()'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Development-specific settings
# Add any development-only apps here if needed
# Example: 'django_extensions', 'debug_toolbar', etc.

