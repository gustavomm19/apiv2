from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TaskView, get_tasks

app_name = 'assignments'
urlpatterns = [
    path('task/', get_tasks),
    path('user/<int:user_id>/task', TaskView.as_view()),
    path('task/<int:task_id>', TaskView.as_view()),
]
