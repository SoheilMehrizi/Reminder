from datetime import datetime
from django.apps import AppConfig

class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    def ready(self):
        from .reminder_scheduler import reminder_updator
        print("Start The Scout...")
        reminder_updator.start()