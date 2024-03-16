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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance.username == username:
            return username
        return super().clean_username()
