from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import userLogin
# Create your views here.

def login(request):
    form = userLogin()
    context = {'form': form}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect("home.html")
        else:
            return HttpResponse("user does not exist")
    return render(request, 'users/login.html', context=context)

def register(request):
    return render(request, 'users/register.html')