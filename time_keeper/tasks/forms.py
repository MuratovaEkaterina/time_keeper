from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput
from django.core.exceptions import ValidationError

class DateTimeInput(DateTimeInput):
    input_type = 'datetime-local'
    
class TaskForm(ModelForm):
    
    class Meta:
        model = Task
        fields = ['text', 'description', 'deadline', 'category']
        widgets = {
            'text': TextInput(attrs={
                'placeholder': 'Задача', 
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Описание', 
                'label': ''
            }), 
            'deadline': DateTimeInput(),
            'category': Select(attrs={
                'placeholder': 'Категория задачи'
            }), 
        }
        
        def clean_text(self):
            text = self.cleaned_data['text']
            if len(text) < 5:
                raise ValidationError('Не указана задача')
            
            return text
      