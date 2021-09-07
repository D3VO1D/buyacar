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
    queryset = CarAdvertisement.objects.all().order_by('-id')
    serializer_class = CarAdSerializer
    pagination_class = CarAdStandardPagination
