from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.decorators import api_view

from To_Do.models import Task


class Task(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'tasks.html', context)


class IndividualDetailTask(View):
    def get(self, request):
        task = Task.objects.get()
        context = {}
        return render(request, )


class SupervisorDetailTask(View):
    def get(self, request):
        task = Task.objects.get()
        context = {}
        return render(request, )


class SupervisorUpdateTask(View):
    def put(self, request):
        task = Task.objects.get()
        return render()


class SupervisorDeleteTask(View):
    pass
