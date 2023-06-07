from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     telegram_nickname = models.CharField(max_length=50)
# account = models.ForeignKey('core.Account', ..)

class Task(models.Model):
    task_text = models.CharField(max_length=70)
    task_description = models.CharField(max_length=300)
    task_deadline = models.DateTimeField('deadline')

class TimeKeeper(models.Model):
    note_time = models.DateTimeField('to note the time')
    spent_time = models.DurationField('spent time')
    
# class Nontification(models.Model):
#     email = models.CharField(max_length=50)
#     telegram_nickname = models.CharField(max_length=50)

# class Authorization(models.Model):
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
    
#категории задач?