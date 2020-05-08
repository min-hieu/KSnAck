from django.shortcuts import render, redirect
from django.contrib import messages
from items.models import transaction
from items.forms import foodOfferForm, foodQueueForm

def home_view(request):
    return render(request, 'home.html', {})

def queue_view(request):
    transactions = transaction.objects.filter(status=3)

    context = {
        'trans' : transactions,
    }

    if request.POST:
        form = foodQueueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added")

            return redirect('queue')
        else:
            context['queue_form'] = form
    else:
        form = foodQueueForm()
        context['queue_form'] = form

    
    return render(request, 'pages/queue.html', context)
    
