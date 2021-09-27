from django.db import models

# Create your models here.
class MessageSender(models.Model):
    email = models.EmailField(
        verbose_name="E-mail", max_length=255, blank=True, null=True
    )
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id} -- {self.email}"
