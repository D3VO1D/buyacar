from rest_framework import viewsets
from django.core.paginator import Paginator

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all()
    serializer_class = CarAdSerializer

    def get_queryset(self):
        p = int(self.request.query_params["p"])
        per_page = 25
        paginator = Paginator(self.queryset, per_page)
        return paginator.page(p)