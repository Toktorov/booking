from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'
        ordering = ('-id',)
