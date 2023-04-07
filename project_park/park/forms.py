from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=50)
    vehicle_name =forms.CharField(max_length=20)
    registration_no = forms.CharField(max_length=10)
    parking_fees = forms.IntegerField()
