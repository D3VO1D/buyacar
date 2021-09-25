from django.db import models


class CarAdvertisement(models.Model):
    source = models.CharField(max_length=128, null=True, blank=True)
    url = models.CharField(max_length=256, null=True, blank=True)
    is_new = models.BooleanField(null=True, blank=True)
    is_broken = models.BooleanField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=128, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photos = models.JSONField(null=True, blank=True, default=list)
    title = models.CharField(max_length=128, null=True, blank=True)
    make = models.CharField(max_length=128, null=True, blank=True)
    model = models.CharField(max_length=128, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    body = models.CharField(max_length=128, null=True, blank=True)
    vin = models.CharField(max_length=128, null=True, blank=True)
    mileage = models.FloatField(null=True, blank=True)
    transmission = models.CharField(max_length=128, null=True, blank=True)
    drive = models.CharField(max_length=128, null=True, blank=True)
    power = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.make, self.model)

    class Meta:
        db_table = 'ads'  # table name in remote db
