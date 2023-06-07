from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_nickname = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "111"
