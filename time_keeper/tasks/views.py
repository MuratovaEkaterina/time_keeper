from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TaskCategory
from .forms import TaskForm, CategoryForm
from django.views.generic import ListView, UpdateView, View
from django.views.generic.edit import FormView, CreateView
#from django.contrib.auth.forms import UserCreationForm

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
            return HttpResponse('Task not found', status=404)
        return redirect('/')

class Category(ListView):
    model = TaskCategory
    template_name = 'categories.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Главная страница'}

class AddCategory(FormView):
    form_class = CategoryForm
    template_name = 'edit_category.html'
    success_url = '/categories'
    extra_context = {'title': 'Добавить категорию'}
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class EditCategory(UpdateView):
    model = TaskCategory
    form_class = CategoryForm
    template_name = 'edit_category.html'    
    success_url = '/categories'
    extra_context = {'title': 'Категории'}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteCategory(View):

    def get(self, _, pk):
        try:
            category = TaskCategory.objects.get(id=pk)
            category.delete()
        except:
            return HttpResponse('Category not found', status=404)
        return redirect('/categories')

# class Registration(FormView):
#     form_class = UserCreationForm
#     template_name = 'registration.html'
    
    




# class Registration(CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration.html'
#     success_url = '/'
    
#     def get_context_data(self, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Регистрация')
#         return dict(list(context.items()) + list(c_def.items()))
    

    
    
    
class Login():
    pass


    
    
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