from django.shortcuts import render
from django.shortcuts import render
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from django.shortcuts import get_object_or_404
from django.db.models import query
from django.core.serializers import serialize
import json
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,

    )
from rest_framework import generics
from rest_framework.generics import ListAPIView


from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)




# def orders_jsonview(APIView):
#     me=request.user
#     mystores=store.objects.filter(driver=me)     
#     newest= order.objects.select_related('store').filter(running_now=True, store__in=mystores).order_by('time_to_pickup')
#     newest.values('store__name','time_to_pickup','adress_to'))  # wrap in list(), because QuerySet is not JSON serializable
#     return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
#     #  order.objects.select_related('store')

# def mystores_jsonview(APIView):
#     mystores=store.objects.filter(driver=user).values('name','adress')
#     data=list(mystores)
#     return JsonResponse(data, safe=False)

# class OrdeListView(generics.CreateAPIView):
#     # user = self.request.user
#     user = 1
#     mystores=store.objects.filter(driver=user)     
#     queryset = order.objects.select_related('store').filter(running_now=True, store__in=mystores).order_by('time_to_pickup')
#     serializer_class = OrderSerializer



# class OrderList_api(generics.ListAPIView):
#     serializer_class = OrderSerializer
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         mystores=store.objects.filter(user_id=user)     
#         print(user.id)
#         print (mystores)
#         newest= order.objects.select_related('store').filter(running_now=True, store__in=mystores).order_by('time_to_pickup')

#         return newest
#         # ('store__name','time_to_pickup','adress_to')

class MyStoreList_api(ListAPIView):

    #mydriver=get_mydriver(self)   
    # myid=user.id
    # mydriver=driver.objects.get(user=myid)
    # myids = mydriver.user_id
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return store.objects.filter(driver=user.driver)

class OrdersReadyToPickup(ListAPIView): 




    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        mystores=store.objects.filter(driver=user.driver)  
        queryset= order.objects.select_related('store').filter(isDelivered=False, store__in=mystores).order_by('time_to_pickup')
        
        return queryset
        
class OrderHistory(ListAPIView):




    serializer_class = OrderHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        mystores=store.objects.filter(driver=user.driver)  
        queryset= order.objects.select_related('store').filter(isDelivered=True ,store__in=mystores).order_by('-created_on')
        
        return queryset 
    


         
























 #mydriver=get_mydriver(self)   
                                                            # myid=user.id
                                                            # mydriver=driver.objects.get(user=myid)
                                                            # myids = mydriver.user_id
    filter_backends =[SearchFilter]

       # user= self.request.user     
        # myid=user.id
        # mydriver=driver.objects.get(user=myid)
        # myids = mydriver.user_id
        # mystores=store.objects.filter(driver__user=1).values('name',
     