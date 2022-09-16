from datetime import datetime
from django.apps import AppConfig


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    def ready(self):
        i=0
        while(i<10):
            now = datetime.now()
            print(now)
            i+=1