from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext as _
from task_manager.users.models import ProjectUser
from task_manager.users.forms import RegistrationForm
from task_manager.users.mixins import CustomUserMixin
from task_manager.mixins import CustomLoginRequiredMixin


class UsersListView(ListView):
    template_name = 'all_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return ProjectUser.objects.exclude(is_staff=True)


class UserCreateView(CreateView):
    template_name = 'create_user.html'
    form_class = RegistrationForm

    def get_success_url(self):
        messages.success(self.request,
                         _('User registered successfully'))
        return (reverse_lazy('login'))


class UserUpdateView(CustomUserMixin,
                     CustomLoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = ProjectUser
    template_name = 'update_user.html'
    form_class = RegistrationForm

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def get_success_url(self):
        messages.success(self.request, _('User successfully changed'))
        return reverse_lazy('all_users')


class UserDeleteView(CustomUserMixin,
                     CustomLoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
    model = ProjectUser
    template_name = 'delete_user.html'

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def get_success_url(self):
        messages.success(self.request, _('User successfully deleted'))
        return reverse_lazy('all_users')
