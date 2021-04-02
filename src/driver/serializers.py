from rest_framework import serializers
from .models import order, store, driver
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order 
        fields=('time_to_pickup', 'adress_to', 'price','create_on', 'finished_on','running_now','store',)

# class DriverSerializer(serializers):
#     pass