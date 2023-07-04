from .models import Task, TaskCategory
from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput
from django import forms

class DateTimeInput(DateTimeInput):
    input_type = 'datetime-local'
    
class TaskForm(ModelForm):
    
    # text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Задача'}), label=False)
    # description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Описание'}), label=False)
    # deadline = forms.DateTimeField(widget=forms.DateTimeInput(), label=False)
    # category = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Категория'}), label=False)

    # class Meta:
    #     model = Task
    #     fields = ['text', 'description', 'deadline', 'category']
    class Meta:
        model = Task
        fields = ['text', 'description', 'deadline', 'category']
        widgets = {
            'text': TextInput(attrs={
                'placeholder': 'Задача', 
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Описание', 
            }), 
            'deadline': DateTimeInput(),
            'category': Select(attrs={
                'placeholder': 'Категория задачи',
            }), 
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = TaskCategory.objects.filter(account=self.initial['account'])
      
class CategoryForm(ModelForm):      
    
    class Meta:
        model = TaskCategory
        fields = ['name', 'description']
        widgets = {
            'name':  TextInput(attrs={
                'placeholder': 'Категория', 
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Описание', 
            }),
            }
        
# class EditTaskForm(ModelForm):
    
#     class Meta:
#         model = Task
#         fields = ['text', 'description', 'deadline', 'category', 'complete']
#         widgets = {
#             'text': TextInput(attrs={
#                 'placeholder': 'Задача', 
#             }), 
#             'description': Textarea(attrs={
#                 'placeholder': 'Описание', 
#             }), 
#             'deadline': DateTimeInput(),
#             'category': Select(attrs={
#                 'placeholder': 'Категория задачи'
#             }), 
#         }
      