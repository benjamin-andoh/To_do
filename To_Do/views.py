from django.shortcuts import render
from rest_framework.decorators import api_view

from To_Do.models import Task


def task(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)
