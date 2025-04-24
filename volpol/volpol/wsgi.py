"""
<<<<<<<< HEAD:volpol/volunteer_platform/wsgi.py
WSGI config for volunteer_platform project.
========
WSGI config for volpol project.
>>>>>>>> origin/volpol:volpol/volpol/wsgi.py

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<<< HEAD:volpol/volunteer_platform/wsgi.py
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
========
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
>>>>>>>> origin/volpol:volpol/volpol/wsgi.py
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<<< HEAD:volpol/volunteer_platform/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volunteer_platform.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volpol.settings')
>>>>>>>> origin/volpol:volpol/volpol/wsgi.py

application = get_wsgi_application()
