from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm

# Create your views here.

# class Registration(FormView):
#     form_class = UserCreationForm
#     template_name = 'registration.html'
#     success_url = '/'

#     def form_valid(self, form):
#         form.save()
#         return super(Registration, self).form_valid(form)

#     def form_invalid(self, form):
#         return super(Registration, self).form_invalid(form)


class Registration(View):
    template_name = 'registration/registration.html'
    extra_context = {'title': 'Регистрация'}

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
