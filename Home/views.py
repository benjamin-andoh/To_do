from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import AllowAny

from Home.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


def login(request):
    pass


def logout(request):
    pass


def home(request):
    return HttpResponse("Hello World")
