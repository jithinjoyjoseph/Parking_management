from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import  HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic import  CreateView,DetailView,UpdateView
from .models import Slots,customer,Registerdcustomer


def index(request):
    return render(request,'base/index.html')


class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

class Slotlist(LoginRequiredMixin,ListView):
    model = Slots
    context_object_name = "park"
    template_name = 'base/slot_list.html'


class CustomerCreate(LoginRequiredMixin,CreateView):
    model = customer
    fields = ['ownername','ownercontact','slot','vehiclecatogary','vehiclename','registration_no','parkingtoken','payment']
    success_url = reverse_lazy('index')
    template_name = 'base/customercreate.html'  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerCreate,self).form_valid(form)  



class Customerlist(LoginRequiredMixin,ListView):
    model = customer
    context_object_name = "customer"
    template_name = 'base/customerlist.html'



class SlotUpdate(LoginRequiredMixin,UpdateView):
    model = Slots
    fields = ['slot_available']
    success_url = reverse_lazy('slots')
    template_name = 'base/slotupdate.html'

    