"""
ASGI config for tutorial_5_relationships_and_hyperlinked_apis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial_5_relationships_and_hyperlinked_apis.settings')

application = get_asgi_application()
