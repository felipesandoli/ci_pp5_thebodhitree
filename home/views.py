from django.shortcuts import render
from property.models import Property

def home(request):
    template = 'home/index.html'
    properties = Property.objects.all() # CHANGE TO ONLY FEATURED PROPERTIES
    context = {
        'properties': properties
    }

    return render(request, template, context)
