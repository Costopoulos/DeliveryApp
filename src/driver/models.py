from django.db import models

class driver(models.Model):
    first_name      = models.CharField(max_length=45)
    last_name       = models.CharField(max_length=45)
    phoneNo         = models.CharField(max_length=15)
    isActive        = models.BooleanField(default=False)
    isBusy          = models.BooleanField(default=False)
   
class store(models.Model):
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
    running_now     = models.BooleanField(default=False)
    store           = models.ForeignKey(store, on_delete=models.CASCADE)