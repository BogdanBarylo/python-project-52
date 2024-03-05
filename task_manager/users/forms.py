from django import forms
from django.forms import ModelForm,TextInput, PasswordInput
from django.core.exceptions import ValidationError
from .models import User


class RegistrationForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'class': 'form-control bs-success-border-subtle'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1' ]
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control bs-success-border-subtle'}),
            'last_name': TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control bs-success-border-subtle'}),
            'username': TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-control bs-success-border-subtle'}),
            'password1': PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control bs-success-border-subtle'})
        }
     
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Введенные пароли не совпадают.")
        elif len(password1) < 3:
            raise ValidationError("Введённый пароль слишком короткий. Он должен содержать как минимум 3 символа.")