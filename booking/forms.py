from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'full_name',
            'email',
            'phone_number',
            'address',
            'city',
            'country',
            'checkin_date',
            'checkout_date',
        ]
