from rest_framework import viewsets

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all()
    serializer_class = CarAdSerializer

    def get_queryset(self):
        p = int(self.request.query_params["p"])
        per_page = 25
        return CarAdvertisement.objects.all()[(p-1)*per_page:p*per_page]