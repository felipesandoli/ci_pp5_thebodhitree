from django.shortcuts import render, get_object_or_404
from property.models import Property
from .forms import BookingForm


def booking(request, property_id):
    """Diplays form for creating a booking and handles form submission"""
    form = BookingForm()
    property = get_object_or_404(Property, pk=property_id)
    template = 'booking/booking.html'
    context = {
        'form': form,
        'property': property,
    }

    return render(request, template, context)
