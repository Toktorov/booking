from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        ordering = ('-id',)
