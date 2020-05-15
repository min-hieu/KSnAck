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


def logoutPage(request):
    logout(request)
    return redirect('/')


def dynamicProfileLookup(request, stuid):
    student = Student.objects.get(student_id=stuid)
    trans_don = transaction.objects.filter(donor=stuid)
    trans_rep = transaction.objects.filter(recipient=stuid)
    context = {
        "student" : student,
        "transdon" : trans_don,
        "transrep" : trans_rep,
    }
    return render(request, "accounts/details.html", context)

def dynamicHistoryLookup(request, stuid):
    trans_don = transaction.objects.filter(donor=stuid, status=1)
    trans_rep = transaction.objects.filter(recipient=stuid, status=1)


    context = {
        "transdon" : trans_don,
        "transrep" : trans_rep,
        "requested_student_id": stuid,
    }
    return render(request, "pages/history.html", context)


def Processing_page(request):

    stuid = request.user.student_id

    trans_pro_re = transaction.objects.filter(status=0, donor=stuid)
    trans_pro_do = transaction.objects.filter(status=0, recipient=stuid)

    context = {
        "trnasprore" : trans_pro_re,
        "trnasprodo" : trans_pro_do,
    }

    return render(request, "pages/processing.html", context)


    

