from django.forms import ModelForm
from .models import Status

class StatusForm(ModelForm):

    class Meta:
        model = Status
        fields = ['name']
        verbose_name = 'Имя'
        verbose_name_plural = 'Имя'
