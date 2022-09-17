from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    path('task/<str:slug>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/<str:slug>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
