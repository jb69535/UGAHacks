from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "cafe/index.html")


def login(request):
    return render(request, "cafe/login.html")

def registration(request):
    return render(request, "cafe/registration.html")

def signup(request):
    return render(request, "cafe/registration.html")