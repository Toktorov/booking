from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, 
        null=True, blank=True
    )

    order = models.ForeignKey(Hotel, 
        on_delete=models.CASCADE, 
        related_name='order',
        blank=True
    )

    create_at = models.DateTimeField(
        auto_now_add=True
    )
    
    arrival_date = models.DateTimeField(
        verbose_name='Дата заезда:'
    )

    departure_date = models.DateTimeField(
        verbose_name='Дата отъезда:',
    )

    name = models.CharField(
        max_length=50,
         verbose_name='Имя:'
    )

    surname = models.CharField(
        max_length=50,
         verbose_name='Фамилия:'
    )

    fatherland = models.CharField(
        max_length = 50,
         verbose_name='Отечество:',
    )

    id_card = models.CharField(
        max_length = 50,
        verbose_name='Паспорт:',
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = 'Брони'
        ordering = ('-create_at', )