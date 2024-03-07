from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name='all_users'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
    path('<int:id>/update/', views.UserUpdateView.as_view(), name='update_user'),
    path('<int:id>/delete/',views.UserDeleteView.as_view(), name='delete_user' ),
]
