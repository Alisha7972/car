from django import forms
from .models import User


class UserForm(forms.ModelForm):
 class Meta:
    
    model = User
    fields = ['name', 'email', 'age', 'notes']
    widgets = {
    'name': forms.TextInput(attrs={'required': True}),
    'email': forms.EmailInput(),
    'age': forms.NumberInput(),
    'notes': forms.Textarea(attrs={'rows':2}),
    }