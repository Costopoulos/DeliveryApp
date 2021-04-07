"""delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from driver import views
from store.views import mydriver_view, order_create_view, today_orders_list
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views
from pages.views import *
from driver.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', mydriver_view),
    path('api/', OrdersReadyToPickup.as_view()),
    path('api/history',OrderHistory.as_view()),
    path('api/stores', MyStoreList_api.as_view()),
    path('create/', order_create_view),
    path('orders/', today_orders_list),
    path('accounts/', include('allauth.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('test/', greeklogin),
]
