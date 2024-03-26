from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, _("You're logged in"))
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    messages.info(request, _("You're unlogged"))
    return redirect('index')
