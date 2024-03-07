from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.users.models import CustomUser
from task_manager.users.forms import RegistrationForm
from django.urls import reverse_lazy


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/all_users.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'users/create_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('all_users')


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'users/update_user.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('all_users')
    pk_url_kwarg = 'id'


class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('all_users')
    pk_url_kwarg = 'id'
