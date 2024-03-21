from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin


class CustomTaskPassesTestMixin(UserPassesTestMixin):

    def handle_no_permission(self):
        task = self.get_object()
        if self.request.user != task.author:
            messages.error(self.request,
                           _('Only the author can delete this task'))
            return redirect('all_tasks')
        return super().handle_no_permission()
