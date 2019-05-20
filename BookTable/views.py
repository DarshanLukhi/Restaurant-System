from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.views.generic import TemplateView
import datetime

from BookTable.models import booktable, genrate
from login.models import register

def BookTable(request):
    if 'name' not in  request.session:
        return HttpResponseRedirect('/login/')
    c = {}
    c.update(csrf(request))
    print("in book_csrf")
    return render(request, 'booktable.html',c)



def proceed(request):
    id=genrate()
    type=request.POST.get('type','')
    people=request.POST.get('people','')
    date=request.POST.get('date','')
    time=request.POST.get('time','')
    p=booktable(id=id,type=type,people=people,date=date,time=time)
    #p.save()

    return render(request,'proceed.html',{'id':id,'type': type, 'people': people, 'date': date, 'time': time})

def done(request):
    print("in done")
    return render(request,'done.html',context=None)