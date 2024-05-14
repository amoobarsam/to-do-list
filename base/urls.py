from django.urls import path


from .views import *

from .views import TaskList , TaskDeatail ,TaskCreate

urlpatterns = [
    path('' , TaskList.as_view(),  name='tasks'),
    path('task/<int:pk>' , TaskDeatail.as_view(),  name='task'),
    path('task-create' , TaskCreate.as_view(),  name='task-create'),
    path('create-task/' , TaskCreate.as_view(),  name='create-task'),


]
