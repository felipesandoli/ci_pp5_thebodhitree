from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:property_id>/', views.booking, name='booking',
    ),
    path('', views.booking, name='booking'),
    path('my_booking/all', views.my_bookings, name='my_bookings'),
    path('booking_details/<booking_number>', views.booking_details, name='booking_details'),
]
