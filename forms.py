from django import forms
from.models import Todo
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['todo_name','todo_content','todo_good_count']
    