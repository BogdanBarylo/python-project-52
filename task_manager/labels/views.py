from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.labels.models import Label
from task_manager.mixins import CustomLoginRequiredMixin


class LabelListView(SuccessMessageMixin, CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = 'all_labels.html'


class LabelCreateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                      CreateView):
    template_name = 'create_label.html'
    model = Label
    fields = ['name']
    success_url = reverse_lazy('all_labels')
    success_message = _('Label successfully created')


class LabelUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin,
                      UpdateView):
    model = Label
    template_name = 'update_label.html'
    fields = ['name']
    success_url = reverse_lazy('all_labels')
    success_message = _('Label successfully changed')


class LabelDeleteView(SuccessMessageMixin, CustomLoginRequiredMixin,
                      DeleteView):
    model = Label
    template_name = 'delete_label.html'
    success_url = reverse_lazy('all_labels')
    success_message = _('Label successfully deleted')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = _('Label successfully deleted')
        if not self.object.task_set.exists():
            self.object.delete()
            messages.success(self.request, success_message)
        else:
            messages.error(self.request,
                           _('Cannot delete a label because it is in use'))
        return redirect('all_labels')
