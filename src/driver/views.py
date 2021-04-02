from django.shortcuts import render
from django.shortcuts import render
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
from .serializers import OrderSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


def get_queryset(self):
    user = self.request.user
    return user.accounts.all()

# def orders_jsonview(APIView):
#     me=request.user
#     mystores=store.objects.filter(driver=me)     
#     newest= order.objects.select_related('store').filter(running_now=True, store__in=mystores).order_by('time_to_pickup')
#     data = list(newest.values('store__name','time_to_pickup','adress_to'))  # wrap in list(), because QuerySet is not JSON serializable
#     return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
#     #  order.objects.select_related('store')

def mystores_jsonview(APIView):
    mystores=store.objects.filter(driver=user).values('name','adress')
    data=list(mystores)
    return JsonResponse(data, safe=False)

class OrdeListView(generics.CreateAPIView):
    # user = self.request.user
    user = 1
    mystores=store.objects.filter(driver=user)     
    queryset = order.objects.select_related('store').filter(running_now=True, store__in=mystores).order_by('time_to_pickup')
    serializer_class = OrderSerializer

    

