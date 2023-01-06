from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, 'contact.html')


def cart(request):
    return render(request, "cart.html")


def home(request):
    return render(request, "index.html")


def checkout(request):
    return render(request, 'checkout.html')

