from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from .models import register
from django.template.context_processors import csrf
from login.models import register

def forgot(request):

    return render(request,'forgot.html',context=None)

def verify(request):
    name = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(name)
    for i in register.objects.all():
        if name==i.username and password==i.password:
            request.session['name'] =i.fName
            request.session['username'] =i.username
            return HttpResponseRedirect('/home/')
        if name==i.gmail and password==i.password:
            request.session['name'] =i.fName
            return HttpResponseRedirect('/home/')
    else:
        return render(request, 'login.html', {'error':'Incorrect Username And Password'})



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def RegisterUser(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    username = request.POST.get('username')
    gmail = request.POST.get('gmail')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')

    for i in register.objects.all():
        if username==i.username:
            return render(request, 'pass.html', {'error':'Username is Already Taken'})
    for i in register.objects.all():
        if gmail==i.gmail:
            return render(request, 'pass.html', {'error':'Gmail Id Is Already Registered'})
    if pass1==pass2:
        s=register(fName=fname,lName=lname,username=username,gmail=gmail,password=pass1)
        s.save()
        return HttpResponseRedirect('/login/')
    else:
        return render(request,'pass.html',{'error':'Your Both Password Is Different'})

def logout(request):
    del request.session['name']
    del request.session['username']
    return HttpResponseRedirect('/home/')

def proceed(request):
    return render(request,'success.html')