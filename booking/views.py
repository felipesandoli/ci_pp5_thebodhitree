from django.shortcuts import render
from property.models import Property
from .forms import BookingForm


def booking(request, property_id):
    """Diplays form for creating a booking"""
    form = BookingForm()
    template = 'booking/booking.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
