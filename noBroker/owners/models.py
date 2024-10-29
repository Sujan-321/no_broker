from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    RESIDENTIAL = 'Residential'
    COMMERCIAL = 'Commercial'
    LAND_PLOT = 'Land/Plot'
    
    PROPERTY_TYPE_CHOICES = [
        (RESIDENTIAL, 'Residential'),
        (COMMERCIAL, 'Commercial'),
        (LAND_PLOT, 'Land/Plot'),
    ]
    
    name = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class PropertyOption(models.Model):
    RENT = 'Rent'
    RESALE = 'Resale'
    PG_HOSTEL = 'PG/Hostel'
    FLATMATES = 'Flatmates'
    SALE = 'Sale'

    RESIDENTIAL_OPTIONS = [(RENT, 'Rent'), (RESALE, 'Resale'), (PG_HOSTEL, 'PG/Hostel'), (FLATMATES, 'Flatmates')]
    COMMERCIAL_OPTIONS = [(RENT, 'Rent'), (SALE, 'Sale')]
    LAND_PLOT_OPTIONS = [(RESALE, 'Resale')]

    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.property_type} - {self.option}"

class Property(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='properties')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='properties')
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='properties')
    option = models.ForeignKey(PropertyOption, on_delete=models.CASCADE, related_name='properties')
    description = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.property_type} in {self.city}, {self.address}\tby {self.owner}"
