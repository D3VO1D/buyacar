from rest_framework import viewsets

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all().order_by('-created_at')
    serializer_class = CarAdSerializer
