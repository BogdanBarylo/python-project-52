from task_manager.users.models import CustomUser
from django import forms


class UserLoginForm(forms.Form):
    model = CustomUser
    username = forms.CharField(label='Имя пользователя', max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)