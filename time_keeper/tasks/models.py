from django.db import models
from django.contrib.auth.models import User 
from core.models import Account

class Task(models.Model):
    text = models.CharField(max_length=70)
    description = models.CharField(max_length=300, blank=True)
    deadline = models.DateTimeField('deadline', null=True, blank=True)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('TaskCategory', on_delete=models.CASCADE, null=True)

class TimeKeeper(models.Model):
    note_time = models.DateTimeField('to note the time', blank=True)
    spent_time = models.DurationField('spent time', blank=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    
    class Meta:
        
        verbose_name_plural = 'Timekeeper'
    
class TaskCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
            

    
