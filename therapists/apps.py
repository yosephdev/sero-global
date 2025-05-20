from django.apps import AppConfig


class TherapistsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'therapists'
    verbose_name = 'Therapists'

    def ready(self):
        import therapists.signals
