from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    telegram_nickname = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Accounts'
