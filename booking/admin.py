from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    readonly_fields = (
        'booking_number',
        'price_total',
        'created_at',
    )

    list_display = (
        'booking_number',
        'full_name',
        'checkin_date',
        'checkout_date',
        'property',
        'price_total',
    )

    ordering = ('-created_at',)


admin.site.register(Booking, BookingAdmin)
