from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from task_manager.users.mixins import CustomLoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class StatusListView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = 'all_statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = 'create_status.html'
    form_class = StatusForm

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно создан')
        return reverse_lazy('all_statuses')


class StatusUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'update_status.html'
    form_class = StatusForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно изменен')
        return reverse_lazy('all_statuses')


class StatusDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete_status.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно удален')
        return reverse_lazy('all_statuses')
