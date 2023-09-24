from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:property_id>/', views.booking, name='booking',
    ),
    path('', views.booking, name='booking'),
    path('my_booking/all', views.my_bookings, name='my_bookings'),
    path(
        'booking_details/<booking_number>',
        views.booking_details,
        name='booking_details'
    ),
    path('search/', views.booking_search, name='booking_search'),
    path('edit/<booking_number>', views.edit_booking, name='edit_booking'),
    path(
        'cancel/<booking_number>',
        views.cancel_booking,
        name='cancel_booking'
    )
]
