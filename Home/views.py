from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request,'home.html',context=None)

def redirect(request):
    return HttpResponseRedirect('home/')
