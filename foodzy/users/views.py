from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

from users.forms import CreateStudentForm,AddBio
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
        
    form = AddBio(request.POST)

    student = Student.objects.get(student_id=stuid)
    transau = transaction.objects.filter(author=stuid)
    transac = transaction.objects.filter(accepter=stuid)
    context = {
        "student" : student, 
        "transau" : transau,
        "transac" : transac,
        "form": form,
    }

    if request.POST and form.is_valid():
        request.user.bio = form.cleaned_data['bio']
        request.user.save()
        redirect('profiles/'+stuid)
    elif request.POST:
        request.user.bio = ""
        request.user.save()

    return render(request, "accounts/details.html", context)


def Processing_page(request,proid=None):
    stuid = request.user.student_id
    trans_au = transaction.objects.filter(status=0,author=stuid)
    trans_ac = transaction.objects.filter(status=0,accepter=stuid)

    context = {
        "transau" : trans_au,
        "transac" : trans_ac,
    }

    if request.POST:
        current_user = request.user
        # princurrent_user.student_id)

        tran_ac = transaction.objects.filter(pk=proid)[0]
        tran_ac.status = 1
        tran_ac.save()

        print("ok1")
        print(tran_ac.author, tran_ac.accepter)

        if tran_ac.author != tran_ac.accepter:
            print("ok")
            author = Student.objects.filter(student_id = tran_ac.author)[0]
            author.happiness += 20
            author.save()

            accepter = Student.objects.filter(student_id = tran_ac.accepter)[0]
            accepter.happiness += 20
            accepter.save()


        
        

    return render(request, "pages/processing.html", context)


    

