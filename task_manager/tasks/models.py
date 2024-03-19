# from django.db import models
# from task_manager.statuses.models import Status
# from task_manager.users.models import ProjectUser
# #from task_manager.labels.models import Label

# class Status(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=150)
#     task_status = models.ForeignKey(Status, null=False)
#     perfomer = models.ForeignKey(ProjectUser, null=True)
#     labels = models.ForeignKey(Label, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

# def __str__(self):
# return self.name
