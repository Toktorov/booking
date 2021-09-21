from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='favorite_users', on_delete=models.SET_NULL)
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='favorite_hotels')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
        ordering = ('-id',)