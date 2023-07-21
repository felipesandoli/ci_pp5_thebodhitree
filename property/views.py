from django.shortcuts import render, get_object_or_404
from .models import Property


def property_details(request, property_id):
    """Displays property full details"""
    property = get_object_or_404(Property, pk=property_id)
    amenities = property.amenities.all()
    template = 'property/property_details.html'
    context = {
        'property': property,
        'amenities': amenities
    }
    return render(request, template, context)
