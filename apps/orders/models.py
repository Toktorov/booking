from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE
    )

    order = models.ForeignKey(Hotel, 
        on_delete=models.CASCADE, 
        related_name='order',
        null = True,
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

    STATUS_CHOICES = (
        ('в обработке', 'в обработке'),
        ('принят', 'принят'),
        ('действительный', 'действительный'),
        ('недействительный', 'недействительный'),
    )

    status = models.CharField(
        choices= STATUS_CHOICES, max_length=255,
        verbose_name='Cтатус заказа:',
        default = 'в обработке'
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Брони'
        verbose_name_plural = 'Брони'
        ordering = ('-create_at', )