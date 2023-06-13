from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    form=TaskForm() 
    if request.method == 'POST':
        form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
    return render(request, 'create_task.html', {'form': form})
