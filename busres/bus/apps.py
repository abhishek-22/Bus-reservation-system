from django.apps import AppConfig


class BusConfig(AppConfig):
    name = 'bus'

    def ready(self):
        import bus.signals
