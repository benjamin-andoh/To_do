from django.urls import path
from To_Do import views

urlpatterns = [
    path('', views.task, name='task'),
    path('json_tasks', views.json_tasks, name='json_tasks'),
    path('get_all_tasks', views.get_all_tasks, name='get_all_tasks')
]