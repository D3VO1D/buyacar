from rest_framework import serializers

from .models import CarAdvertisement


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertisement
        fields = ['id', 'source', 'url', 'is_new', 'is_broken', 'price', 'location', 'latitude', 'longitude',
                  'photos', 'title', 'make', 'model', 'year', 'body', 'vin', 'mileage', 'transmission',
                  'drive', 'power']


class MakesSerializer(serializers.Serializer):
    make = serializers.CharField(max_length=200)
