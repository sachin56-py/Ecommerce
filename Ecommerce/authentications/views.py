from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import userLogin, UserRegisterForm
from .models import User
# Create your views here.

def login(request):
    form = userLogin()
    context = {'form': form}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            return redirect("home.html")
        else:
            return HttpResponse("user does not exist")
    return render(request, 'users/login.html', context=context)

def register(request):
    form = UserRegisterForm()
    context = {'form': form}
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.contact = request.POST.get("contact")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
        return redirect('index.html')
    return render(request, 'users/register.html', context=context)