
from django.urls import path
from . import views
from .views import CustomLogin, download_invoice
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('', views.parking_slots, name='parking_slots'),
    path('customer-details/', views.customer_details, name='customer_details'),
    path('add-customer/<int:slot_id>/', views.add_customer, name='add_customer'),
    path('remove-customer/<int:customer_id>/', views.remove_customer, name='remove_customer'),
    path('history/', views.history, name='history'),
    path('download-invoice/<int:customer_id>/', views.download_invoice, name='download_invoice'),

]
