import django

__version__ = '0.22.1a'

if django.VERSION < (3, 2):
    default_app_config = 'drf_spectacular.apps.SpectacularConfig'
