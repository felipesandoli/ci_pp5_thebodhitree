from django.db import models
from django_countries.fields import CountryField
from property.models import Property
import uuid


class Booking(models.Model):
    booking_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    full_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)
    city = models.CharField(max_length=120, null=False, blank=False)
    country = CountryField(null=False, blank=False)
    checkin_date = models.DateField(null=False, blank=False)
    checkout_date = models.DateField(null=False, blank=False)
    number_of_guests = models.IntegerField(null=False, blank=False, default=0)
    property = models.ForeignKey(
        Property, null=False, blank=False, on_delete=models.CASCADE
    )
    price_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.booking_number

    # From boutique ado
    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_price_total(self):
        """Calculates price total based on stay duration"""
        # price is calculated by number of nights,
        # time delta gives number of days, so take away 1
        length_of_stay = (self.checkout_date - self.checkin_date).days - 1
        print(length_of_stay)
        self.price_total = self.property.price_per_night * length_of_stay

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the booking number
        if not yet set
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)
