from django.shortcuts import render
from property.models import Property

def home(request):
    template = 'home/index.html'
    featured_properties = Property.objects.filter(feature=True)
    context = {
        'properties': featured_properties
    }

    return render(request, template, context)
