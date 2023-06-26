from django.db import models
from django.contrib.auth.models import User 
from core.models import Account
from django.core.validators import MinLengthValidator

class Task(models.Model):
    text = models.CharField(max_length=70, validators=[MinLengthValidator(limit_value=5, message='От 5 символов')])
    description = models.CharField(max_length=300, blank=True)
    deadline = models.DateTimeField('deadline', blank=True, null=True)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return f'Task({self.id}) {self.text}'
    

class TimeKeeper(models.Model):
    note_time = models.DateTimeField('to note the time', blank=True)
    spent_time = models.DurationField('spent time', blank=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name_plural = 'Timekeeper'
    
class TaskCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
            

    
