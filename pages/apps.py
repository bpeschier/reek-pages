from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class PagesAppConfig(AppConfig):
    name = 'pages'

    def ready(self):
        # Walk over all views-modules to discover views
        autodiscover_modules('views')
