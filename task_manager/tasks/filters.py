import django_filters
from django import forms
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from django.utils.translation import gettext as _


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='filter_self_tasks',
        label=_('Only my tasks')
    )

    label = django_filters.filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Labels')
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['task_status', 'executor', 'label', 'self_tasks']
