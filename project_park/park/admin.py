

# Register your models here.

#orionparking
#jithinjoy98



from django.contrib import admin

from .models import Customer, History, ParkingSlot

# Register your models here.
#orionparking
#jithinjoy98

admin.site.register(ParkingSlot),
admin.site.register(Customer),
admin.site.register(History)