from django.shortcuts import render
from items.models import transaction

def dynamicItemView(request, proid):
    obj = transaction.objects.get(food_id=proid)
    context = {
        "transaction": obj,
    }
    return render(request, "items/details.html", context)

def ProductByStudentView(request, stu_id):
    trans = transaction.objects.get(donor=stu_id)
    context = {
        "trans": trans,
    }
    return render(request, "items/history.html", context)
