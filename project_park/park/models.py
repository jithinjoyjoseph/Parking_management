from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Slots(models.Model):
    
    name = models.CharField(max_length=200)
    floor= models.CharField(max_length=200)
    slot_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    




class customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True ,blank=True)
    ownername = models.CharField(max_length=50)
    ownercontact = models.CharField(max_length=15)
    vehiclecatogary =models.CharField(max_length=20)
    vehiclename =models.CharField(max_length=20)
    registration_no = models.CharField(max_length=10)
    parkingtoken = models.IntegerField()
    park_date = models.DateField(auto_now_add=True)
    intime = models.TimeField(auto_now_add=True)
    payment=models.BooleanField(default=False)
    slot = models.ForeignKey(Slots,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    


    def __str__(self):
        return self.ownername
    

class Registerdcustomer(models.Model):
    ownername = models.ForeignKey(customer, on_delete=models.CASCADE,null=True ,blank=True)
    slot= models.ForeignKey(Slots,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)

