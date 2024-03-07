from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control bs-success-border-subtle'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control bs-success-border-subtle'}),
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-control bs-success-border-subtle'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control bs-success-border-subtle'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control bs-success-border-subtle'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'class': 'form-control bs-success-border-subtle'}),
        }
