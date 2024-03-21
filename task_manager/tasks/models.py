from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import ProjectUser
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(max_length=300, null=True, blank=True,
                                   verbose_name=_('Description'))
    task_status = models.ForeignKey(Status, on_delete=models.PROTECT,
                                    verbose_name=_('Status'))
    executor = models.ForeignKey(ProjectUser, on_delete=models.PROTECT,
                                 null=True, blank=True,
                                 verbose_name=_('Executor'))
    author = models.ForeignKey(ProjectUser, on_delete=models.PROTECT,
                               related_name='creator',
                               verbose_name=_('Author'))
    timestamp = models.DateTimeField(auto_now_add=True)
