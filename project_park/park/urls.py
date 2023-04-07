from django.contrib import admin
from django.urls import path, include

from .views import CustomLogin
from . import views
from django.contrib.auth.views import LogoutView
from . views import Slotlist,CustomerCreate,SlotUpdate,Customerlist

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('slots/',Slotlist.as_view(),name='slots'),
    path('customer',CustomerCreate.as_view(),name='customer'),
    path('customerlist/',Customerlist.as_view(),name='customer-list'),
    path('slotupdate/<int:pk>/', SlotUpdate.as_view(), name="slotupdate"),
]