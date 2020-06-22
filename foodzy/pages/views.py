from django.shortcuts import render, redirect
from django.contrib import messages
from items.models import transaction
from items.forms import foodQueueForm
from users.models import Student
from taggit.models import Tag


def home_view(request):
    rankings = Student.objects.order_by('-happiness', 'student_id')[:10]
    context = {
            'rankings' : rankings,
            }

    return render(request, 'home.html', context)

def queue_view(request,proid=None,method=None):
    transactions = transaction.objects.filter(status=3)
    tags = Tag.objects.all()

    q = request.GET.get('q', '')
    typ = request.GET.get('typ', '')
    if q:
        if typ:
             q = q.split()
             transactions = transactions.filter(tags__name__in=q).filter(method=int(typ)).distinct()
        else:
            q = q.split()
            transactions = transactions.filter(tags__name__in=q).distinct()
    else:
        if typ: transactions = transactions.filter(method=int(typ))
        else: transactions = transactions.all()
    q = ''
    context = {
            'trans' : transactions,
            'q': q,
            'tags': tags,
            'typ': typ
            }    

    if request.POST.get('title'):
        form = foodQueueForm(request.POST)
        if form.is_valid() and form.cleaned_data['author']:
            form.cleaned_data['author']
            form.save()
            messages.success(request, " successfully added ")
            return redirect('queue')
        else:
            context['queue_form'] = form
    elif request.POST and method:
        if method == 'apply':
            current_user = request.user
            tran_ac = transaction.objects.filter(pk=proid)[0]
            tran_ac.status = 0
            tran_ac.accepter = current_user.student_id
            tran_ac.save()
        if method == 'remove':
            current_user = request.user
            query = transaction.objects.filter(pk=proid)[0]
            query.delete()


        return redirect('queue')

    else:
        form = foodQueueForm()
        context['queue_form'] = form

    

    
    return render(request, 'pages/queue.html', context)