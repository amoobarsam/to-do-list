from django.urls import path

from .views import TaskList , TaskDeatail

urlpatterns = [
    path('' , TaskList.as_view(),  name='tasks'),
    path('task/<int:pk>' , TaskDeatail.as_view(),  name='task'),
]
