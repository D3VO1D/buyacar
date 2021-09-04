from django.db import models


class CarAdvertisement(models.Model):
    brand = models.CharField(max_length=128)
    price = models.IntegerField()
    production_year = models.IntegerField()
    # etc
    created_at = models.DateTimeField(auto_now_add=True)
    # source, location, etc...
