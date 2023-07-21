from django.db import models
from django_countries.fields import CountryField
from property.models import Property


class Booking(models.Model):
    booking_number = models.CharField(
        max_length=16, null=False, editable=False
    )
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    country = CountryField(null=False, blank=False)
    checkin_date = models.DateField(null=False, blank=False)
    checkout_date = models.DateField(null=False, blank=False)
    property = models.ForeignKey(
        Property, null=False, blank=False, on_delete=models.CASCADE
    )
    price_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )

    def __str__(self):
        return self.booking_number