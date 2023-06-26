from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TaskCategory
from .forms import TaskForm, CategoryForm
from django.views.generic import ListView, UpdateView, View
from django.views.generic.edit import FormView, CreateView
from django.db.models import ProtectedError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная страница'}
    
    def get_queryset(self):
        if not self.request.user:
            return HttpResponse('ошибка доступа!', status=401)
        return self.model.objects.filter(account=self.request.user.id)

    

class CreateTask(LoginRequiredMixin, FormView):
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/'
    extra_context = {'title': 'Создать задачу'}
    login_url = '/login'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.account = self.request.user
        task.save()
        return redirect(self.success_url)
    
    # def get_initial(self) -> dict[str, Any]:
    #     s = super().get_initial()
    #     return s
    
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
        except TaskCategory.DoesNotExist:
            return HttpResponse('Category not found', status=404)
        except ProtectedError as e:
            return HttpResponse(f'Protected Category: {", ".join(map(str, e.protected_objects))}', status=400)
        except Exception as e:
            return HttpResponse(e, status=500)
        return redirect('/categories')


    



    
    
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