from django.contrib import admin

# Register your models here.
from .models import store,driver,order
admin.site.register(driver)
admin.site.register(store)
admin.site.register(order)