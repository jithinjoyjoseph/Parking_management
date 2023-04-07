from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse
from reportlab.pdfgen import canvas


from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from io import BytesIO

from .models import Customer

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import ParkingSlot, Customer, History
from .forms import CustomerForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


def index(request):
    return render(request,'index.html')


class CustomLogin(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
    

def parking_slots(request):
    slots = ParkingSlot.objects.all()
    context = {'slots': slots}
    return render(request, 'parking_slots.html', context)

def customer_details(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer_details.html', context)



def add_customer(request, slot_id):
    slot = ParkingSlot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact = form.cleaned_data['contact']
            customer = Customer(name=name, contact=contact, parking_slot=slot)
            customer.save()
            slot.is_available = False
            slot.save()
            return redirect('download_invoice',customer_id =customer.id)
    else:
        form = CustomerForm()
    context = {'form': form, 'slot': slot}
    return render(request, 'add_customer.html', context)




def remove_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    slot = customer.parking_slot
    customer.delete()
    slot.is_available = True
    slot.save()
    history = History(name=customer.name, contact=customer.contact, parking_slot=customer.parking_slot.name, occupied_time=customer.occupied_time, left_time=datetime.now())
    history.save()
    return redirect('customer_details')

def history(request):
    history = History.objects.all()
    context = {'history': history}
    return render(request, 'history.html', context)



    


def download_invoice(request, customer_id):
    # Get the customer object
    customer = get_object_or_404(Customer, id=customer_id)

    # Render the HTML template with the customer data
    template = get_template('invoice_template.html')
    context = {
        'customer': customer,
    }
    html = template.render(context)

    # Create a PDF file from the HTML template
    pdf_file = BytesIO()
    p = canvas.Canvas(pdf_file)
    p.drawString(100, 750, "Invoice")

    p.drawString(100, 650, f"Name: {customer.name}")
    p.drawString(100, 600, f"Contact: {customer.contact}")
    p.drawString(100, 550, f"Parking slot: {customer.parking_slot.name}")
    p.showPage()
    p.save()

    # Send the PDF file as a response with appropriate headers
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    filename = f"{customer.name}_invoice.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response
    

