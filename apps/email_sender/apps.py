from tabnanny import verbose
from django.apps import AppConfig


class EmailSenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.email_sender'
    verbose_name = "Отправка сообщений"
