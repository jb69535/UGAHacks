import login as login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, "cafe/index.html")


def login(request):
    return render(request, "cafe/login.html")

def registration(request):
    return render(request, "cafe/registration.html")

def signup(request):
    return render(request, "cafe/registration.html")

def success_page(request):
    return render(request, 'success_page.html')

def buttonaction(request):
    if request.method == 'POST':
        username = request.POST['Email']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success_page')
        else:
            return render(request, 'form.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'form.html')