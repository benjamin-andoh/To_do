from django.urls import path
from Home.views import register, home
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', home, name='home'),
    path('', register, name='register'),

    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
