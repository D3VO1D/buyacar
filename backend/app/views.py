from rest_framework import viewsets

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all()
    serializer_class = CarAdSerializer

    def get_queryset(self):
        p = int(self.request.query_params["p"])
        cars_on_page = 50
        return CarAdvertisement.objects.all()[(p-1)*cars_on_page:p*cars_on_page]