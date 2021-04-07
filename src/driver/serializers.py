from rest_framework import serializers
from .models import order, store, driver
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order 
        fields=('time_to_pickup', 'adress_to', 'price','running_now','store',)

# class DriverSerializer(serializers):
#     pass

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = store 
        fields=( 'name', 'adress','phone', )       

class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields=('time_to_pickup', 'adress_to', 'price','running_now','store','created_on','finished_on','running_now','isDelivered')