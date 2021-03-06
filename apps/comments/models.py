from django.db import models
from apps.hotels.models import Hotel
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='reply_comment', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -- {self.text}"

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
        ordering = ['-comment_created']

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        