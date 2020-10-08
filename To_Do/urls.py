from django.urls import path
from To_Do.views import Task

urlpatterns = [
    path('', Task.as_view(), name='task'),


]