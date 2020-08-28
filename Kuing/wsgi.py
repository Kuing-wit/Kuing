"""
WSGI config for Kuing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
>>>>>>> 0dba6de278cc942757987caf9defdca13e083497
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kuing.settings')

application = get_wsgi_application()
