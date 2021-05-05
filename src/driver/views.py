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
from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,

    )
from rest_framework import generics
from rest_framework.generics import ListAPIView,UpdateAPIView


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


class OrderPickedUp(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class= OrderPickedUpSerializer
    lookup_field= 'id'


    def get_queryset(self):
        user = self.request.user
        mystores=store.objects.filter(driver=user.driver)  
        queryset= order.objects.select_related('store').filter(running_now=False ,store__in=mystores)
        
        return queryset 

class OrderDelivered(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class= OrderDeliveredSerializer
    lookup_field= 'id'


    def get_queryset(self):
        user = self.request.user
        mystores=store.objects.filter(driver=user.driver)  
        queryset= order.objects.select_related('store').filter(isDelivered=False ,store__in=mystores)
        
        return queryset 
            
                


# class IsTheDriverOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the owner of the snippet.
#         return obj.user == request.user.id



# class DriverUpdate(UpdateAPIView):
#     permission_classes = [IsAuthenticated,IsTheDriverOrReadOnly]
#     serializer_class= DriverUpdateSerializer
#     lookup_field= 'user'

#     def get_queryset(self):
#         queryset=driver.objects.all()  
    
        
#         return queryset 

from rest_framework import generics, mixins, permissions

# User = get_user_model()

class UserIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user.id

class UserProfileChangeAPIView(generics.RetrieveAPIView,
                               mixins.DestroyModelMixin,
                               mixins.UpdateModelMixin):
    permission_classes = (
        permissions.IsAuthenticated,
        UserIsOwnerOrReadOnly,
    )
    serializer_class = DriverUpdateSerializer
    # parser_classes = (MultiPartParser, FormParser,)

    def get_object(self):
        user = self.kwargs["user"]
        obj = get_object_or_404(driver, user=user)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
























 #mydriver=get_mydriver(self)   
                                                            # myid=user.id
                                                            # mydriver=driver.objects.get(user=myid)
                                                            # myids = mydriver.user_id

       # user= self.request.user     
        # myid=user.id
        # mydriver=driver.objects.get(user=myid)
        # myids = mydriver.user_id
        # mystores=store.objects.filter(driver__user=1).values('name',
     