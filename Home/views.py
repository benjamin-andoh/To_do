from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from Home.forms import Register


def register(request):
    form = Register()
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context,)





# def login(request):



def logout(request):
    pass


def home(request):
    return HttpResponse("Hello World")
