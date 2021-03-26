from django.shortcuts import render
from django.views import View
from driver.models import store,driver,order
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from .forms import OrderForm




myid=1

def mydriver_view(request):
    myid=1
      # get the current date
    today = datetime.today()
    orders = order.objects.all()
    obj= driver.objects.get(id=1)
    context = { 
        'name' : obj.first_name,
        'lastname' : obj.last_name,
        'phone' : obj.phoneNo,
        'active'  :  obj.isBusy        
    }
    
    return render(request, "mydriver.html", context) 

def order_create_view(request):
    form=OrderForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = { 
        'form': form
    }
    return render( request, "order_create.html", context)


def today_orders_list(request):
    today=datetime.today()
    print(today.time)
    queryset=order.objects.all()
    context ={
        "object_list": queryset
    }
    return render(request, "order_list.html", context)