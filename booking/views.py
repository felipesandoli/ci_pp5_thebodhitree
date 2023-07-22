from django.shortcuts import render, get_object_or_404, redirect
from property.models import Property
from .forms import BookingForm


# from property details page property id is passed as a parameter
def booking(request, property_id=None):
    """Diplays form for creating a booking and handles form submission"""
    if request.method == 'GET':
        form = BookingForm()
        property = None
        if property_id:
            property = get_object_or_404(Property, pk=property_id)
        template = 'booking/booking.html'
        context = {
            'form': form,
            'property': property
        }

        return render(request, template, context)
    else:
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'country': request.POST['country'],
            'checkin_date': request.POST['checkin_date'],
            'checkout_date': request.POST['checkout_date'],
            'number_of_guests': request.POST['number_of_guests'],
            'property': get_object_or_404(Property, name=request.POST['property']),
        }
        print(form_data)
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.update_price_total()
            booking.save()
            return redirect('home')
        else:
            # error message
            pass
