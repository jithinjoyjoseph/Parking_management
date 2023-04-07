from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=50)
