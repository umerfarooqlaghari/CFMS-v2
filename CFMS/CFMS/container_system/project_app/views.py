from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CargoType, Port,  FAQ, Booking, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from .forms import bookingform
from .forms import TrackingForm
from .forms import SignupForm,  CustomAuthenticationForm
from .forms import FAQForm
from django.db import transaction
from django.db.models import F
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request, *args, **kwargs):
    return render(request,"project_app/index.html")


def home(request, *args, **kwargs):
    return render(request,"project_app/home.html")

#
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            print(f"Username: {username}, Password: {password}")

            if user is not None:
                login(request, user)
                print("Login successful")
                return redirect('booking')
            else:
                messages.error(request, 'Invalid username or password.')
                print("Authentication failed")
        else:
            messages.error(request, 'Invalid form submission. Please check the fields and try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'project_app/login.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:

                transaction.set_autocommit(False)


                form.save()
                username = form.cleaned_data.get('username')


                transaction.commit()

                messages.success(request, f'Account created for {username}! You can now log in.')
                return redirect('login')  

            except Exception as e:

                transaction.rollback()


                messages.error(request, f'Error creating account: {e}')

            finally:

                transaction.set_autocommit(True)

    else:
        form = SignupForm()

    return render(request, 'project_app/register.html', {'form': form})
#
@login_required
def booking(request):
    if request.method == 'POST':
        template_name = 'project_app/booking.html'  
        form = bookingform(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Start the transaction
                booking = form.save(commit=False)


                if request.user.is_authenticated:
                    booking.user = request.user
                    booking.save()


                    booking_id = booking.id
                    weight = form.cleaned_data['weight']
                    tax = 17
                    base_shipment_cost = 2000


                    cost = calculate_booking_cost(weight, tax, base_shipment_cost)

                    confirmation_message = f'Thank you for your booking! Your booking ID is {booking_id}. ' \
                                           f'Your estimated cost is {cost}. We will contact you soon.'


                    messages.success(request, confirmation_message)

                transaction.commit()

                return redirect('track')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = bookingform()

    context = {'form': form}
    return render(request, 'project_app/booking.html', context)

    
    


def track(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            booking_id = form.cleaned_data['booking_id']
            try:
                order = Order.objects.select_related('booking').get(booking__booking_id=booking_id)
                weight = order.booking.weight
                tax = 17
                base_shipment_cost = 2000


                cost = calculate_booking_cost( weight, tax, base_shipment_cost)

            except Order.DoesNotExist:
                order = None
            context = {'form': form, 'order': order}
            return render(request, 'project_app/tracking.html', context)
    else:
        form = TrackingForm()
        context = {'form': form}
        return render(request, 'project_app/tracking.html', context)



def details(request):
    
    ports = Port.objects.all()

    context = {
        'ports': ports
    }
    return render(request,"project_app/details.html", context)

def calculate_booking_cost( weight, tax, base_shipment_cost):
        
        doubled_weight = F(weight) * 5
        doubled_tax = F(tax) / 10
        cost1 = doubled_weight + base_shipment_cost 
        cost=(cost1*(doubled_tax))+cost1
        return cost


def about_us(request):
    faqs = FAQ.objects.all()

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.user = request.user  # Assuming the current user is asking the question
            faq.save()
            return redirect('/about_us')

    else:
        form = FAQForm()

    context = {
        'form': form,
        'faqs': faqs
    }
    
    return render(request, 'project_app/about_us.html', context)

