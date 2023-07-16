from django.db import models
from django_countries.fields import CountryField


class Amenity(models.Model):

    class Meta:
        verbose_name_plural = 'Amenities'

    name = models.CharField(max_length=20)


class Property(models.Model):

    class Meta:
        verbose_name_plural = 'Properties'

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    country = CountryField()
    single_beds = models.IntegerField(null=True, blank=True)  # Number of single beds in property
    double_beds = models.IntegerField(null=True, blank=True)  # Number of double beds in property
    rooms = models.IntegerField(null=True, blank=True)        # Number of non suite rooms
    suites = models.IntegerField(null=True, blank=True)       # Number of suites
    bathrooms = models.IntegerField(null=True, blank=True)    # Number of bathrooms except suites
    amenities = models.ManyToManyField(Amenity, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    # Featured properties to be displayed on home page
    feature = models.BooleanField(default=False)
    # Main property image
    featured_image = models.ImageField()

    def __str__(self):
        return self.name


class Image(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='gallery'
    )
    # Description to be used on alt attribute
    description = models.CharField(max_length=250)
    image = models.ImageField()
