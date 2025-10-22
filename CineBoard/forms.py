from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Films

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['image', 'title', 'description', 'genre', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
