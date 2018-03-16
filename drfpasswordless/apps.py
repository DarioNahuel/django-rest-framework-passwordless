from django.apps import AppConfig


class DrfpasswordlessConfig(AppConfig):
    name = 'customdrfpasswordless'

    def ready(self):
        import drfpasswordless.signals  # NOQA
