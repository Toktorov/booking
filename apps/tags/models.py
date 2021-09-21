from django.db import models
from apps.hotels.models import Hotel

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)
    hotels = models.ManyToManyField(Hotel)

    def __str__(self):
        return f"{self.title} {self.hotels}"

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
        ordering = ('-id',)
