from rest_framework import serializers

from .models import CarAdvertisement


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdvertisement
        fields = "__all__"
