from django.contrib import admin
from .models import Task, TaskCategory, TimeKeeper

admin.site.register(Task)
admin.site.register(TimeKeeper)
admin.site.register(TaskCategory)
