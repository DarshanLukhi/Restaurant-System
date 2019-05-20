from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView




def AboutUs(request):

    if 'name' not in request.session:
        return render(request, 'about.html',context=None)
    else:
        name=request.session['name']
        return render(request,'about.html',{"name":name})
