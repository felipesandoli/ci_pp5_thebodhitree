from django.db import models
from django_countries.fields import CountryField


class Amenity(models.Model):

    class Meta:
        verbose_name_plural = 'Amenities'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name.replace('_', ' ')


class Property(models.Model):

    class Meta:
        verbose_name_plural = 'Properties'

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    country = CountryField()
    # Number of single beds in property
    single_beds = models.IntegerField(null=True, blank=True)
    # Number of double beds in property
    double_beds = models.IntegerField(null=True, blank=True)
    # Number of non suite rooms
    rooms = models.IntegerField(null=True, blank=True)
    # Number of suites
    suites = models.IntegerField(null=True, blank=True)
    # Number of bathrooms except suites
    bathrooms = models.IntegerField(null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    is_available = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    # Featured properties to be displayed on home page
    feature = models.BooleanField(default=False) # is_featured
    # Main property image
    featured_image = models.ImageField()

    def __str__(self):
        return self.name
    
    def number_of_bedrooms(self):
        return self.rooms + self.suites
    
    def number_of_bathrooms(self):
        return self.bathrooms + self.suites


class Image(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name='gallery'
    )
    # Description to be used on alt attribute
    description = models.CharField(max_length=250)
    image = models.ImageField()
