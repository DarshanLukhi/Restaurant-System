import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect

from login.models import register
from .models import Food

p=[]


def FoodOrder(request):

    if 'name' not in  request.session:
        return HttpResponseRedirect('/login/')


    c = {}
    c.update(csrf(request))

    typefood = request.POST.get('typefood')

    if str(typefood)=='None':
        typefood='Fast Food'
    detail = Food.objects.filter(category=typefood)
    c = {'detail': detail}


    for i in Food.objects.all():

        temp=request.GET.get(str(i.id))
        if str(temp)=='None' or temp=='':
            continue
        x='username_id='

        name=request.session['username']

        ob=Food.objects.get(id=i.id)

        x+=name
        x+=",category="
        x+=ob.category
        x+=',quantity='
        x+=str(temp)
        x+=",price="
        x+=ob.price


        #p.append(x)
        print(x)
    return render(request, 'foodorder.html',c)


