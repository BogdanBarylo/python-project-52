from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.users.models import ProjectUser
from task_manager.users.forms import RegistrationForm
from task_manager.users.mixins import CustomUserPassesTestMixin
from task_manager.mixins import CustomLoginRequiredMixin


class UsersListView(ListView):
    template_name = 'all_users.html'

    def get_queryset(self):
        return ProjectUser.objects.exclude(is_staff=True)


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'create_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')


class UserUpdateView(SuccessMessageMixin,
                     CustomUserPassesTestMixin,
                     CustomLoginRequiredMixin,
                     UserPassesTestMixin,
                     UpdateView):
    model = ProjectUser
    template_name = 'update_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('all_users')
    success_message = _('User successfully changed')

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user


class UserDeleteView(SuccessMessageMixin,
                     CustomUserPassesTestMixin,
                     CustomLoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
    model = ProjectUser
    template_name = 'delete_user.html'
    success_message = _('User successfully deleted')
    success_url = reverse_lazy('all_users')

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, args, kwargs)
        except ProtectedError:
            messages.error(request,
                           _('Cannot delete the user because it is in use'))
        return redirect('all_users')
