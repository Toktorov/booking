from django.db import models
from apps.countries.models import Country
from django.contrib.auth import get_user_model
from apps.tags.models import Tag

User = get_user_model()

# Create your models here.
class Hotel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name = 'hotels_user',
        null=True, blank=True
    )

    title = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name='Название:'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )

    price = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=1
    )

    PAYMENT_CHOICES = (
        ('USD', 'USD'),
        ('EURO', 'EURO'),
        ('KGZ', 'KGZ'),
        ('RUB', 'RUB'),
    )

    payment = models.CharField(
        choices=PAYMENT_CHOICES, max_length=255,
        verbose_name='Оплата валюта:',
        default = 'USD'
    )

    WIFI_CHOICES = (
        ('Есть', 'Есть'),
        ('Отсутствует', 'Отсутствует'),
    )

    wifi = models.CharField(
        choices=WIFI_CHOICES, max_length=255,
        verbose_name='Wifi:',
        default = 'Отсутствует'
    )

    PARKING_CHOICES = (
        ('Есть', 'Есть'),
        ('Отсутствует', 'Отсутствует'),
    )

    parking = models.CharField(
        choices=PARKING_CHOICES, max_length=255,
        verbose_name='Парковка:',
        default = 'Отсутствует'
    )

    FRONT_DESK_CHOICES = (
        ('Есть', 'Есть'),
        ('Отсутствует', 'Отсутствует'),
    )

    front_desk = models.CharField(
        choices=FRONT_DESK_CHOICES, max_length=255,
        verbose_name='Круглосуточная стойка регистрации:',
        default = 'Отсутствует'
    )

    FAMILY_ROOMS_CHOICES = (
        ('Есть', 'Есть'),
        ('Отсутствует', 'Отсутствует'),
    )

    family_rooms = models.CharField(
        choices=FAMILY_ROOMS_CHOICES, max_length=255,
        verbose_name='Семейные номера:',
        default = 'Отсутствует'
    )

    NON_SMOKING_ROOMS_CHOICES = (
        ('Есть', 'Есть'),
        ('Отсутствует', 'Отсутствует'),
    )

    non_smoking_rooms = models.CharField(
        choices=NON_SMOKING_ROOMS_CHOICES, max_length=255,
        verbose_name='Номера для некурящих:',
        default = 'Отсутствует'
    )

    contact_number = models.CharField(
        max_length = 50, 
        verbose_name = "Контактный номер",
    )

    tags = models.ManyToManyField(Tag, related_name='hotel_tags', blank = True)

    created = models.DateTimeField(
        auto_now_add=True
    )

    countries = models.ForeignKey(
        Country,
        related_name='hotel_country',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Отели'
        verbose_name_plural = 'Отели'
        ordering = ('-created',)

    def __str__(self):
        return f"{self.title}"

    def get_parent(self):
        return self.comment.filter(parent__isnull=True)
        
class HotelImage(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='hotel_image'
    )

    image = models.ImageField(
        upload_to='hotel_image',
        verbose_name='Фото отеля'
    )

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_user')
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes_hotel')


    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Лайки'
        verbose_name_plural = 'Лайки'
        ordering = ('-id',)
