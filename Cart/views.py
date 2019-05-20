import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from FoodOrder.models import Food
from login.models import register

def cart(request):
    try:
        amount = 0
        cartdata =Food.objects.filter(id=request.session['uid'])
        for i in cartdata:
            amount = amount + i.quantity * i.price

        if amount == 0:
            return render(request, 'cart.html', {'msg': 'Your Cart is Empty', 'amount': amount})
        else:
            return render(request, 'cart.html', {'cart': cartdata, 'amount': amount})
    except Exception:
        return render(request, 'login.html', {'msg': 'Login to view your Cart!'})


def pay(request):
    return render(request, 'payment.html')


def bill(request):
    return render(request, 'bill.html')


def add(request):
    return HttpResponseRedirect('/Cart/')
'''
def add(request):
    id = request.session['uid']
    item = request.POST.get('item')
    quantity = request.POST.get('quantity')
    qu = ProductDescription.objects.get(p_id=item)
    price = qu.price
    for i in OrderDetails.objects.all():
        if i.p_id == qu:
            i.quantity = int(i.quantity) + int(quantity)
            i.save()
            return HttpResponseRedirect('/Cart/')
    q = OrderDetails(
        user_id=uid,
        o_date=datetime.datetime.now(),
        price=price,
        p_id=qu,
        quantity=quantity,
        images=qu.images,
        item=qu.item,
    )
    q.save()
    return HttpResponseRedirect('/Cart/')


def remove(request):
    uid = request.session['uid']
    item = request.POST.get('item')
    qu = ProductDescription.objects.get(id=item)
    for i in OrderDetails.objects.all():
        if i.p_id == qu and uid == i.user_id:
            i.delete()
            return HttpResponseRedirect('/Cart/')
    return HttpResponseRedirect('/Cart/')'''