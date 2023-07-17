from django.shortcuts import render, get_object_or_404
from .models import Property


def property_details(request, id):
    """Displays property full details"""
    property = get_object_or_404(Property, pk=id)
    template = 'property/property_details.html'
    context = {
        'property': property
    }
    return render(request, template, context)
