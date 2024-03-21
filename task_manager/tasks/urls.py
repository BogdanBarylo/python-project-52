from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('',
         views.TasksListView.as_view(), name='all_tasks'),
    path('create/',
         views.TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/',
         views.TaskDetailView .as_view(), name='task_information'),
    path('<int:pk>/update/',
         views.TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/',
         views.TaskDeleteView.as_view(), name='delete_task'),
]
