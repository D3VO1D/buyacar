from rest_framework import serializers

from .models import CarAdvertisement


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertisement
        fields = ('id', 'brand', 'price', 'production_year', 'created_at')
