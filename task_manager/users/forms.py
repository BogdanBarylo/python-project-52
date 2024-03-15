from .models import ProjectUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = ProjectUser
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2']
