from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSeriazer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description',
                  'start_date', 'developer']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'email', 'first_name',
                 'last_name ']
