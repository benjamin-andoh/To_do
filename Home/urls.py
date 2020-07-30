from django.urls import path
from Home import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.UserCreate.as_view())
]
