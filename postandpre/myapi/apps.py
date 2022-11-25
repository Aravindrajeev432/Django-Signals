from django.apps import AppConfig


class MyapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapi'

    def ready(self):
        import myapi.signals

# In settings.py add app like 'myapi.apps.MyapiConfig'
# 'myapi' will not work
