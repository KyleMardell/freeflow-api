from django.urls import path
from tasks import views

urlpatterns = [
    path('projects/<int:project_id>/tasks/', views.TaskList.as_view()),
    path('projects/<int:project_id>/tasks/<int:pk>/', views.TaskDetail.as_view()),
]