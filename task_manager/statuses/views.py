from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.mixins import CustomLoginRequiredMixin
from task_manager.statuses.models import Status


class StatusListView(SuccessMessageMixin, CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = 'all_statuses.html'


class StatusCreateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                       CreateView):
    template_name = 'create_status.html'
    model = Status
    fields = ['name']
    success_url = reverse_lazy('all_statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                       UpdateView):
    model = Status
    template_name = 'update_status.html'
    fields = ['name']
    success_url = reverse_lazy('all_statuses')
    success_message = _('Status successfully changed')


class StatusDeleteView(SuccessMessageMixin, CustomLoginRequiredMixin,
                       DeleteView):
    model = Status
    template_name = 'delete_status.html'
    success_url = reverse_lazy('all_statuses')
    success_message = _('Status successfully deleted')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = _('Status successfully deleted')
        if not self.object.task_set.exists():
            self.object.delete()
            messages.success(self.request, success_message)
        else:
            messages.error(self.request,
                           _('Cannot delete a status because it is in use'))
        return redirect('all_statuses')
