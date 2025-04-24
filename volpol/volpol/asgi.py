"""
<<<<<<<< HEAD:volpol/volunteer_platform/asgi.py
ASGI config for volunteer_platform project.
========
ASGI config for volpol project.
>>>>>>>> origin/volpol:volpol/volpol/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<<< HEAD:volpol/volunteer_platform/asgi.py
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
========
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
>>>>>>>> origin/volpol:volpol/volpol/asgi.py
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:volpol/volunteer_platform/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volunteer_platform.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volpol.settings')
>>>>>>>> origin/volpol:volpol/volpol/asgi.py

application = get_asgi_application()
