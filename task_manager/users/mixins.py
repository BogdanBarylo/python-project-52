from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    error_message = ('Вы не авторизованы! Пожалуйста, выполните вход.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.error_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request,
                           'У вас нет прав для изменения другого пользователя')
            return redirect('all_users')
        else:
            return redirect('login')
