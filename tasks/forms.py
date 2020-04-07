from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'new_task_text', 'placeholder': 'Add new task'}),
        }


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'new_task_text'}),
        }