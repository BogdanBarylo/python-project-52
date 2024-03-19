from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CustomUserMixin:

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You do not have permissions to modify another user'))
            return redirect('all_users')
        else:
            return redirect('login')
