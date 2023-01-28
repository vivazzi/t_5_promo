import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 't_5_promo.settings')

application = get_wsgi_application()
