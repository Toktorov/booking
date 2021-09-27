from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Men'),
        ('f', 'Female'),
    )
    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(upload_to='profiles', blank=True, null=True)
    age = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length = 100, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=255)

    def __str__(self):
        return f"{self.username}{self.gender}"

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)
