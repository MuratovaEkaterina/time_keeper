from django.db import models
from django.contrib.auth.models import User 
from core.models import Account
from django.core.validators import MinLengthValidator
from django.utils import timezone
import datetime


class Task(models.Model):
    text = models.CharField(max_length=70, validators=[MinLengthValidator(limit_value=5, message='От 5 символов')])
    description = models.CharField(max_length=300, blank=True)
    deadline = models.DateTimeField('deadline', blank=True, null=True)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('TaskCategory', on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return f'Task({self.id}) {self.text}'
    
    @property
    def started(self):
        for tk in self.timekeepers.all():
            if tk.started:
                return True
        return False
    
    @property
    def spent_time(self):
        counter = datetime.timedelta(0)
        for tk in self.timekeepers.all():
            counter += tk.spent_time
        return counter
            
        



class TimeKeeper(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, related_name='timekeepers')
    start = models.DateTimeField('start', blank=False, null=False)
    end = models.DateTimeField('end', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Timekeeper'
        
    @property
    def started(self):
        return self.start is not None and self.end is None
    
    @property
    def spent_time(self):
        if self.end is None:
            return timezone.now() - self.start
        return self.end - self.start
    

    
    
        

# def spent_time(request):
       
    # def start(self):
    #     task = TimeKeeper(text=text)
    #     task.start = timezone.now()
    #     task.save()
    #     return task.start
    
    # def end(text):
    #     task = TimeKeeper(text=text)
    #     task.end = timezone.now()
    #     task.end()
    #     return task.start
    
    # def spent_time(text):
    #     task = TimeKeeper(text=text)
    #     spent_time = task.end - task.start
    #     return spent_time

        
    

    
class TaskCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150, blank=True)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
            

    
