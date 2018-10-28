from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'animeinfo.core'

    def ready(self):
        from . import signals
