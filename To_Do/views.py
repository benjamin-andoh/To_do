from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from To_Do.models import Task
from To_Do.serializer import TaskSeriazer


def task(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, "tasks.html", context)


@api_view(['GET', ])
def json_tasks(request):
    tasks = {
        1: {'title': 'To Do 1', 'done': False, 'responsible_username': 'janis', 'created_by_username': 'Ulrich'},
        2: {'title': 'To Do 2', 'done': False, 'responsible_username': 'janis', 'created_by_username': 'Ulrich'},
        3: {'title': 'To Do 3', 'done': False, 'responsible_username': 'Eric', 'created_by_username': 'Janis'},
        4: {'title': 'To Do 4', 'done': True, 'responsible_username': 'Eric', 'created_by_username': 'Ulrich'}
    }
    return Response(tasks)


@api_view(['GET', ])
def get_all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSeriazer(tasks, many=True)
    return Response(serializer.data)


