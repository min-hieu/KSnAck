from django.shortcuts import render
from .models import transaction

def dynamic_lookup_view(request, my_id):
    obj = transaction.objects.get(id=my_id)
    context = {
        "object": obj,
    }
    return render(request, "items/details", context)

def ProductByStudentView(request, stu_id):
    trans = transaction.objects.get(donor=stu_id)
    context = {
        "trans": trans,
    }
    return render(request, "items/history", context)
