from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class CustomUserPassesTestMixin(UserPassesTestMixin):

    def handle_no_permission(self):
        if self.request.user != self.get_object():
            messages.error(
                self.request,
                _('You do not have permissions to modify another user'))
            return redirect('all_users')
        return super().handle_no_permission()
