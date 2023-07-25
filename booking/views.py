from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from property.models import Property
from .models import Booking
from .forms import BookingForm


# from property details page property id is passed as a parameter
def booking(request, property_id=None):
    """Diplays form for creating a booking and handles form submission"""
    if request.method == 'POST':
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
            'property': get_object_or_404(
                Property, name=request.POST['property']
            ),
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.update_price_total()
            booking.save()
            return redirect(
                'booking_details', booking_number=booking.booking_number
            )
        else:
            # error message
            pass
    else:
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


@login_required
def my_bookings(request):
    """Displays to an authenticated user bookings created by them"""
    bookings = Booking.objects.filter(user=request.user)
    template = 'booking/my_bookings.html'
    context = {
        'bookings': bookings,
    }
    return render(request, template, context)


def booking_details(request, booking_number):
    """Displays details about a specific booking"""
    booking = get_object_or_404(Booking, booking_number=booking_number)
    template = 'booking/booking_details.html'
    context = {
        'booking': booking,
    }
    return render(request, template, context)


def booking_search(request):
    """Displays a search form for users without an account
    to find their bookings and handles booking search submission"""
    if request.method == 'POST':
        booking_number = request.POST['booking_number'].split()[0]
        booking = Booking.objects.filter(booking_number=booking_number)
        if booking:
            print(booking)
            return redirect('booking_details', booking_number=booking_number)
        else:
            return redirect('booking_search')
    else:
        template = 'booking/booking_search.html'
        return render(request, template)

 
def edit_booking(request, booking_number):
    """
    Displays form for editing guest personal information only.
    """
    if request.method == 'POST':
        booking = get_object_or_404(Booking, booking_number=booking_number)
        form = BookingForm(request.POST)
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        if form.is_valid:
            booking.full_name = full_name
            booking.email = email
            booking.phone_number = phone_number
            booking.address = address
            booking.city = city
            booking.country = country
            booking.save()
        return redirect('booking_details', booking_number=booking_number)
    else:
        booking = get_object_or_404(Booking, booking_number=booking_number)
        booking_form = BookingForm(instance=booking)
        template = 'booking/edit_booking.html'
        context = {
            'booking': booking,
            'form': booking_form,
        }
        return render(request, template, context)
