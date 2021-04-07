from django.db import models
from django.contrib.auth.models import User

class driver(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    phoneNo         = models.CharField(max_length=15)
    isActive        = models.BooleanField(default=False)
    isBusy          = models.BooleanField(default=False)
   
class store(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    name            = models.CharField(max_length=45)
    adress          = models.CharField(max_length=1024)
    phone           = models.CharField(max_length=15)
    driver          = models.ForeignKey(driver, on_delete=models.CASCADE)

class order(models.Model):
    time_to_pickup  = models.DateTimeField (blank=False)
    adress_to       = models.CharField(max_length=1024)
    price           = models.DecimalField(max_digits=7, decimal_places=2)
    created_on      = models.DateTimeField(auto_now_add=True)
    finished_on     = models.DateTimeField(auto_now=True)
    running_now     = models.BooleanField(default=False) #picked_up
    store           = models.ForeignKey(store, on_delete=models.CASCADE)
    isDelivered     = models.BooleanField(default=False)
