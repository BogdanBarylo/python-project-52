from task_manager.users.models import User
from django.forms import ModelForm, TextInput, PasswordInput


class UserLoginForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password1']

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-control bs-success-border-subtle'}),
            'password1': PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control bs-success-border-subtle'}),
        }