from django.shortcuts import render, redirect
from django.contrib import messages
from items.models import transaction
from items.forms import foodOfferForm, foodQueueForm
from users.models import Student

def home_view(request):
    rankings = Student.objects.order_by('-happiness', 'student_id')[:10]
    context = {
            'rankings' : rankings,
            }

    return render(request, 'home.html', context)

def queue_view(request,proid=None):
    transactions = transaction.objects.filter(status=3)

    context = {
        'trans' : transactions,
    }

    if request.POST.get('title'):
        print(request.POST.get('title'))
        form = foodQueueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added")

            return redirect('queue')
        else:
            context['queue_form'] = form
    elif request.POST and proid:
        current_user = request.user
        tran_ac = transaction.objects.filter(pk=proid)[0]
        tran_ac.status = 2
        tran_ac.donor = current_user.student_id
        tran_ac.save()

        return redirect('queue')

    else:
        form = foodQueueForm()
        context['queue_form'] = form

    

    
    return render(request, 'pages/queue.html', context)
    
