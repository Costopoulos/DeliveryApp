from django.shortcuts import render
from django.views import View
from driver.models import store,driver,order
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from .forms import OrderForm
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import messages



myid=1

def mydriver_view(request):

    user=request.user

    mystore=store.objects.get(user_id=user)
    obj= mystore.driver

    context = { 
        'store' : mystore.name,
        'storeaddress': mystore.adress,
        'name' : obj.first_name,
        'lastname' : obj.last_name,
        'phone' : obj.phoneNo,
        'active'  :  obj.isBusy ,
        'username'  : user.username
               
    }
    
    return render(request, "mydriver.html", context) 

def order_create_view(request):
    form=OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        #instance.order = request.user.id
        #instance.order = request.user.driver
        
        #instance.order = request.user.store
        instance.store = request.user.store
        instance.save()
        messages.success(request, "Η παραγγελία δημιουργήθηκε")
        return HttpResponseRedirect('http://localhost:8000/orders/')

    context = { 
        'form': form
    }
    return render( request, "order_create.html", context)


def today_orders_list(request):
    user=request.user
    today=datetime.today()
    mystore=store.objects.get(user_id=user)
    queryset=order.objects.filter(store=mystore)
    context ={
        "object_list": queryset
    }
    return render(request, "order_list.html", context)

    from django.utils import timezone
from django.views.generic.list import ListView




