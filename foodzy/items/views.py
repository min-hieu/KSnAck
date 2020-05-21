from django.shortcuts import render
from items.models import transaction

def dynamicItemView(request, proid):
    obj = transaction.objects.get(id=proid)
    context = {
        "transaction": obj,
    }
    return render(request, "items/details.html", context)

