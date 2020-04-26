from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from users.forms import CreateStudentForm

def registerPage(request):
    context = {}

    if request.POST:
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            student_id = form.cleaned_data.get('student_id')
            raw_password = form.cleaned_data.get('password1')
            student = authenticate(student_id=student_id, password = raw_password)
            login(request, student)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = CreateStudentForm()
        context['registration_form'] = form
        
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def userHome(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
