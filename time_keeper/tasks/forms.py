from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select, DateInput

class DateInput(DateInput):
    input_type = 'date'
    
class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ['text', 'description', 'deadline', 'category']
        
        widgets = {
            'text': TextInput(attrs={
                'placeholder': 'Задача'
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Описание'
            }), 
            'deadline': DateInput(), 
            'category': Select(attrs={
                'placeholder': 'Категория задачи'
            }), 
        }