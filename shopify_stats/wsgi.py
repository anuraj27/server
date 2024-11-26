# shopify_stats/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'shopify_stats' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_stats.settings')

# Get the WSGI application for the Django project.
application = get_wsgi_application()

