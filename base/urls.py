from django.urls import path
from .views import *



urlpatterns = [
    path('' , TaskList.as_view(),  name='tasks'),
    path('task/<int:pk>' , TaskDeatail.as_view(),  name='task'),
    path('task-create' , TaskCreate.as_view(),  name='task-create'),
    path('task-update/<int:pk>' , UpdaTask.as_view(),  name='task-update'),
   


]
