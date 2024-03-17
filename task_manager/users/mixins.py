from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    error_message = (_('You are not authorized! Please log in.'))

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.error_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You do not have permissions to modify another user'))
            return redirect('all_users')
        else:
            return redirect('login')
