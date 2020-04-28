from django.shortcuts import render
from items.models import transaction

def home_view(request):
    return render(request, 'home.html', {})

def queue_view(request):
    transactions = transaction.objects.filter(status=3)
    context = {
        'trans' : transactions,
    }
    return render(request, 'items/queue.html', context)
    
