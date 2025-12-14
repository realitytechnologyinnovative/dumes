"""
Django settings for dume project.

This module imports the appropriate settings based on the environment.
"""

import os

# Determine which settings to use
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *


