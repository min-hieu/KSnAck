from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from users.forms import CreateStudentForm
from users.models import Student
from items.models import transaction
from django.contrib import messages

def registerPage(request):
    context = {}

    if request.POST:
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            student_id = form.cleaned_data.get('student_id')
            messages.success(request, 'Account was registered for ' + student_id)

            return redirect('login')

        else:
            context['registration_form'] = form
    else:
        form = CreateStudentForm()
        context['registration_form'] = form

    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}

    if request.POST:
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        student = authenticate(request, student_id=student_id, password=password)
        
        if student is not None:
            login(request, student)
            return redirect('/')

    context = {}
    return render(request, 'accounts/login.html', context)

def userHome(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')


def dynamicProfileLookup(request, stuid):
    student = Student.objects.get(student_id=stuid)
    context = {
        "student" : student
    }
    return render(request, "accounts/details.html", context)

def dynamicHistoryLookup(request, stuid):
    transactions = transaction.objects.filter(donor=stuid)
    context = {
        "trans" : transactions
    }
    return render(request, "items/history.html", context)
    

