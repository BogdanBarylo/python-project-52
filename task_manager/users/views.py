from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.models import User
from task_manager.users.forms import RegistrationForm


class UsersView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/all_users.html',
            context={'users': users})


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'users/create_user.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        return render(request, 'users/create_user.html', {'form': form})


class UserUpdateView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user =  User.objects.get(id=user_id)
        form = RegistrationForm(instance=user)
        return render(request, 'users/update_user.html', {'form': form, 'user_id': user_id})
    

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('all_users')
        return render(request, 'users/update_user.html', {'form': form, 'user_id': user_id})


class UserDeleteView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(request, 'users/delete_user.html', {'user': user})


    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('all_users')
