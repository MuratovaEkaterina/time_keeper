from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, TaskCategory, TimeKeeper
from .forms import TaskForm, CategoryForm #EditTaskForm
from django.views.generic import ListView, UpdateView, View
from django.views.generic.edit import FormView, CreateView
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


class Index(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная страница'}
    login_url = '/login'
    
    def get_queryset(self):
        if not self.request.user:
            return HttpResponse('Ошибка доступа!', status=401)
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
    
    def get_initial(self) -> dict[str, Any]:
        s = super().get_initial()
        s['account'] = self.request.user
        return s
    
class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'    
    success_url = '/'
    extra_context = {'title': 'Редактировать задачу'}
    login_url = '/login'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
    def get_queryset(self):
        if not self.request.user:
            return HttpResponse('Ошибка доступа!', status=401)
        return self.model.objects.filter(account=self.request.user.id)

class DeleteTask(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, _, pk):
        try:
            task = Task.objects.get(id=pk, account=self.request.user.id)
            task.delete()
        except TaskCategory.DoesNotExist:
            return HttpResponse('Task not found', status=404)
        except ProtectedError as e:
            return HttpResponse(f'Protected Task: {", ".join(map(str, e.protected_objects))}', status=400)
        except Exception as e:
            return HttpResponse(e, status=500)
        return redirect('/')
    
    # def get_queryset(self):
    #     if not self.request.user:
    #         return HttpResponse('Ошибка доступа!', status=401)
    #     return self.model.objects.filter(account=self.request.user.id)
    
class Category(LoginRequiredMixin, ListView):
    model = TaskCategory
    template_name = 'categories.html'
    context_object_name = 'categories'
    extra_context = {'title': 'Категории'}
    login_url = '/login'
    
    def get_queryset(self):
        if not self.request.user:
            return HttpResponse('Ошибка доступа!', status=401)
        return self.model.objects.filter(account=self.request.user.id)
    
class CreateCategory(LoginRequiredMixin, FormView):
    form_class = CategoryForm
    template_name = 'edit_category.html'
    success_url = '/categories'
    extra_context = {'title': 'Добавить категорию'}
    login_url = '/login'
    
    def form_valid(self, form):
        category = form.save(commit=False)
        category.account = self.request.user
        category.save()
        return redirect(self.success_url)
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
class EditCategory(LoginRequiredMixin, UpdateView):
    model = TaskCategory
    form_class = CategoryForm
    template_name = 'edit_category.html'    
    success_url = '/categories'
    extra_context = {'title': 'Категории'}
    login_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteCategory(LoginRequiredMixin, View):
    login_url = '/login'
    
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


class Start(LoginRequiredMixin, View):
    login_url = '/login'
    def get(self, _, pk):
        try:
            task = Task.objects.get(id=pk, account=self.request.user.id)                
        except TaskCategory.DoesNotExist:
            return HttpResponse('Task not found', status=404)
        except Exception as e:
            return HttpResponse(e, status=500)
        if not task.started:
            timekeeper = TimeKeeper(task=task, start=timezone.now())
            try:
                timekeeper.save()
            except Exception as e:
                return HttpResponse(e, status=500)
        return redirect('/')
        
            
    model = TimeKeeper
    template_name = 'index.html'
    context_object_name = 'start'
    
    @property
    def start(self):
        return self.start
    
    
class End(ListView):
    model = TimeKeeper
    template_name = 'index.html'
    context_object_name = 'end'
    
    def set_end(self):
        self.end = timezone.now()

    def get_end(self):
        return self.end
    
    start = property(get_end, set_end)
    
    
    
# class SpentTime():
#     model = TimeKeeper
#     def set_start(self):
#         self.start = timezone.now()

#     def get_start(self):
#         return self.start
    
#     start = property(get_start, set_start)
    
#     def set_end(self):
#         self.end = timezone.now()

#     def get_end(self):
#         return self.end
    
#     end = property(get_end, set_end)
    


# def spent_time(request):
#     return render(request, 'index.html', TimeKeeper.end - TimeKeeper.start)
