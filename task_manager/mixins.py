from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    error_message = (_('You are not authorized! Please log in.'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.error_message)
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
