from django.db import models
from django.db.models.signals import pre_save
from utils.slug_generator import unique_slug_generators

# Create your models here.
class Country(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )

    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'
        ordering = ('-id',)

class CountryImage(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_image'
    )

    image = models.ImageField(
        upload_to='country_image',
        verbose_name='Фото отеля'
    )


def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Country)