from django import forms
from .models import Booking


# from stackoverflow
class DateInput(forms.DateInput):
    input_type = 'date'


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
            'number_of_guests',
        ]
        widgets = {
            'checkin_date': DateInput(),
            'checkout_date': DateInput(),
        }
