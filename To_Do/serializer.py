from django.contrib.auth.models import User
from rest_framework import serializers
from To_Do.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description',
                  'start_date', 'developer', 'supervisor']


class UserSerializer(serializers.ModelSerializer):
    supervisor = TaskSerializer(many=True, readonly=True)
    developer = TaskSerializer(many=True, readonly=True)

    class Meta:
        model = User
        field = ['username', 'email', 'first_name',
                 'last_name ', 'supervisor', 'developer']

