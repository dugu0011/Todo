from argparse import Namespace
from decimal import Clamped
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','tech58.settings')

app = Celery('tech58')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

