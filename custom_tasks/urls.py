from django.urls import path
from custom_tasks import views

urlpatterns = [
    path('custom_tasks/', views.CustomTaskList.as_view()),
    path('custom_tasks/<int:pk>/', views.CustomTaskDetail.as_view()),
]
