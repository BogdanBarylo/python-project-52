from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView, DetailView)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from task_manager.tasks.mixins import CustomTaskPassesTestMixin
from task_manager.tasks.models import Task
from task_manager.mixins import CustomLoginRequiredMixin


class TasksListView(CustomLoginRequiredMixin, ListView):
    model = Task
    template_name = 'all_tasks.html'


class TaskDetailView(CustomLoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_information.html'


class TaskCreateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                     CreateView):
    template_name = 'create_task.html'
    model = Task
    fields = ['name', 'description', 'task_status', 'executor', 'labels']
    success_url = reverse_lazy('all_tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                     UpdateView):
    model = Task
    template_name = 'update_status.html'
    fields = ['name', 'description', 'task_status', 'executor', 'labels']
    success_url = reverse_lazy('all_tasks')
    success_message = _('Task successfully changed')


class TaskDeleteView(SuccessMessageMixin,
                     CustomLoginRequiredMixin,
                     CustomTaskPassesTestMixin,
                     DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('all_tasks')
    success_message = _('Task successfully deleted')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
