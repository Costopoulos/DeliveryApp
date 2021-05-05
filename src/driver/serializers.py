from rest_framework import serializers
from .models import order, store, driver
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order 
        fields=('id','time_to_pickup', 'adress_to', 'price','running_now','store')

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

class OrderPickedUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = order 
        fields=('id','running_now')

class OrderDeliveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = order 
        fields=('id','isDelivered','finished_on')


class DriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=driver
        fields=('user','isActive','realHourStart','realHourEnd')

# class DriverPickedUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=driver
#         fields('id','isBusy')

# class 

from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

# # class UserProfileChangeSerializer(ModelSerializer):
# #     username = CharField(required=False, allow_blank=True, initial="current username")
# #     class Meta:
# #         model = User
# #         fields = [
# #             'username',
# #             'password',
# #         ]