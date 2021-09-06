from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all()
    serializer_class = CarAdSerializer

    def get_queryset(self):
        try:
            p = int(self.request.query_params["p"])
        except MultiValueDictKeyError:
            p = 1
        per_page = 25
        paginator = Paginator(self.queryset, per_page)
        try:
            page = paginator.page(p)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        return page