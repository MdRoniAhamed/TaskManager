from django.urls import path, include
from .api import views
from . import views as v

urlpatterns = [
    path('api/',include('task.api.urls')),
    path('',v.task_show, name='task_show'),
    path('add/',v.add_task, name='add_task'),
    path('<int:pk>/',v.delete_task, name='delete'),
    path('complete/<int:pk>/',v.completed, name='complete'),
    path('searching/',v.Searching, name='search'),
    path('filtering/',v.filtering, name='filter'),
]
