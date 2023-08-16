from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_token = models.CharField(max_length=255, blank=True, null=True)
    telegram_id = models.CharField(max_length=255, blank=True, null=True)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.sender.user.username} - {self.timestamp}"
