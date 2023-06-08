from django.db import models
from django.contrib.auth.models import User 
from core.models import Account

class Task(models.Model):
    task_text = models.CharField(max_length=70)
    task_description = models.CharField(max_length=300, blank=True)
    task_deadline = models.DateTimeField('deadline')
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)
    task_category = models.ForeignKey('TaskCategory', on_delete=models.CASCADE, null=True)

class TimeKeeper(models.Model):
    note_time = models.DateTimeField('to note the time', blank=True)
    spent_time = models.DurationField('spent time', blank=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    
    class Meta:
        
        verbose_name_plural = 'Timekeeper'
    
class TaskCategory(models.Model):
    task_category_name = models.CharField(max_length=15)
    task_category_description = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    
