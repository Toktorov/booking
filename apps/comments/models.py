from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.text}"

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
        ordering = ['-comment_created']