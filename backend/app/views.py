from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import CarAdvertisement
from .serializers import CarAdSerializer


class CarAdStandardPagination(PageNumberPagination):
    page_size = 50

    def get_paginated_response(self, data):
        # adding field totalPages to response
        response = super(CarAdStandardPagination, self).get_paginated_response(data)
        response.data['totalPages'] = self.page.paginator.num_pages
        return response


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
    pagination_class = CarAdStandardPagination
