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
    def ended(self):
        for tk in self.timekeepers.all():
            if tk.ended:
                return True
        return False
    
    @property
    def spent_time(self):
        counter = datetime.timedelta(0)
        for tk in self.timekeepers.all():
            counter += tk.spent_time
        return counter
    
    @property
    def spent_time_str(self):
        seconds = self.spent_time.total_seconds()
        result = ''
        if seconds >= 60 * 60 * 24:
            days = int(seconds // (60 * 60 * 24))
            result += f'{days} дней '
            seconds -= days * (60 * 60 * 24)
        if seconds >= 60 * 60:
            hours = int(seconds // (60 * 60))
            result += f'{hours} часов '
            seconds -= hours * 60 * 60
        if seconds >= 60:
            minutes = int(seconds // 60)
            result += f'{minutes} минут '
            seconds -= minutes * 60
        seconds = int(seconds)
        if seconds > 0:
            result += f'{seconds} секунд'
        return result


class TimeKeeper(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, related_name='timekeepers')
    start = models.DateTimeField('start', blank=False, null=False)
    #  start = models.DateTimeField('start', blank=False, null=False)     NOT NULL constraint failed: tasks_timekeeper.start
    end = models.DateTimeField('end', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Timekeeper'

    @property
    def started(self):
        return self.start is not None and self.end is None

    @property
    def ended(self):
        return self.end is not None and self.start is not None

    @property
    def spent_time(self):
        if self.end is None and self.start is not None:
            return timezone.now() - self.start
        return self.end - self.start


class TaskCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150, blank=True)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
