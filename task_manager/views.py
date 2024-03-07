from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


class HomePageView(TemplateView):
     template_name = "index.html"


class LoginView(View):
    
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
          form = UserLoginForm(request.POST)
          if form.is_valid():
               username = request.POST.get('username')
               password1 = request.POST.get('password1')
               user = authenticate(request, username=username, password1=password1)
               if user is not None:
                    login(request, user)
                    return redirect('index.html')
          return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('index.html')
