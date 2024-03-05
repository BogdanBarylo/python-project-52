from django.forms import ModelForm,TextInput
from .models import Status

class StatusForm(ModelForm):

    class Meta:
        model = Status
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control bs-success-border-subtle'})}