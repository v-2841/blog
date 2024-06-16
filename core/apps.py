from django.apps import AppConfig
from django.db.backends.signals import connection_created

from core.utils import load_icu


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        connection_created.connect(load_icu)
