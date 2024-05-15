from uuid import uuid4
from django import forms
from .models import  Booking, CargoType, Port, FAQ
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
        })
    )
class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
        })
    )

    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['pick_up_location', 'destination', 'cargo_type_name', 'weight', 'booking_email_id', 'booking_phone']
        widgets = {
            'pick_up_location': forms.Select(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'cargo_type_name': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'booking_email_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'booking_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        if self.instance and self.instance.user:
            self.fields['booking_email_id'].initial = self.instance.user.email
            # Assuming the Booking model has a user attribute with a phone_number field
            self.fields['booking_phone'].initial = self.instance.user.phone_number


class TrackingForm(forms.Form):
    booking_id = forms.CharField(label='Booking ID', max_length=9)
        
        
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['query','user_email','user_name']
        
        