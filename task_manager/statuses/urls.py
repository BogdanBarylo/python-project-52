from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesView.as_view(), name='all_statuses'),
    path('create/', views.StatusCreateView.as_view(), name='create_status'),
    path('<int:id>/update/', views.StatusUpdateView.as_view(), name='update_status'),
    path('<int:id>/delete/',views.StatusDeleteView.as_view(), name='delete_status' ),
]
