from django.shortcuts import render


def property_details(request, id):
    """Displays property full details"""
    template = 'property/property_details.html'
    return render(request, template)
