from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.users.models import ProjectUser
from task_manager.users.forms import RegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from task_manager.users.mixins import CustomLoginRequiredMixin


class UsersListView(ListView):
    model = ProjectUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'users/create_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class UserUpdateView(CustomLoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProjectUser
    template_name = 'users/update_user.html'
    form_class = RegistrationForm
    pk_url_kwarg = 'id'


    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
    

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно изменен')
        return reverse_lazy('update_user', kwargs={'id': self.object.id})


class UserDeleteView(CustomLoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProjectUser
    template_name = 'users/delete_user.html'
    pk_url_kwarg = 'id'


    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно удален')
        return reverse_lazy('all_users')
