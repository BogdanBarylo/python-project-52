from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from task_manager.forms import UserLoginForm
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = UserLoginForm


    def form_valid(self, form):
        messages.success(self.request, 'Вы залогинены')
        return super().form_valid(form)
        

def logout_user(request):
    logout(request)
    messages.info(request, 'Вы разлогинены')
    return redirect('index')
