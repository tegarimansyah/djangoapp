from django.apps import AppConfig

from health_check.plugins import plugin_dir
from .metrics import APP_VERSION


class UtilsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.utils"

    def ready(self) -> None:
        from .healthcheck import MyDatabaseBackend, HTTPBinCheck

        plugin_dir.register(MyDatabaseBackend)
        plugin_dir.register(HTTPBinCheck)
