from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def userHome(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
