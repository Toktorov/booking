from tabnanny import verbose
from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.countries'
    verbose_name = "Города"