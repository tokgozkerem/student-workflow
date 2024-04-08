"""
URL configuration for coursescheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from numpy import delete
from courses.views import (
    delete_assignment_view,
    home_view,
    add_course_view,
    add_assignment_view,
    delete_assignment_view,
    start_pomodoro,
    todo_list,
    delete_task,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("add-course/", add_course_view, name="add_course"),
    path("add-assignment/", add_assignment_view, name="add_assignment"),
    path("delete_assignment/", delete_assignment_view, name="delete_assignment"),
    path("pomodoro/", start_pomodoro, name="pomodoro"),
    path("todo_list/", todo_list, name="todo_list"),
    path("delete_task/<int:pk>/", delete_task, name="delete_task"),
]
