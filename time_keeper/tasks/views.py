from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, UpdateView, View
from django.views.generic.edit import FormView
from django.contrib import messages

class Index(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная страница'}
    

class CreateTask(FormView):
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/'
    extra_context = {'title': 'Создать задачу'}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EditTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'    
    success_url = '/'
    extra_context = {'title': 'Редактировать задачу'}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class DeleteTask(View):

    def get(self, _, pk):
        try:
            task = Task.objects.get(id=pk)
            task.delete()
        except:
            return HttpResponse("Task not found", status=404)
        return redirect('/')


    


# def edit_task(request, pk):
#     form = TaskForm
#     return render(request, 'edit_task.html', {'form': form})


# class EditTask(FormView):
#     form_class = TaskForm
#     template_name = 'index.html'
#     success_url = '/'
    
#     def get_initial(self):
#         initial = super().get_initial()
#         id = self.kwargs.get('id')
        
#         return initial
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)