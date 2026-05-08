import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BloodDonation.settings')
django.setup()

from django.apps import apps
for app in apps.get_app_configs():
    print(app.label)
