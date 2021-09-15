from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Min, Count
from collections import Counter

from .models import CarAdvertisement
from .serializers import CarAdSerializer
from .filters import CarAdFilter
from .services import get_client_ip, get_ip_details, get_models_and_count, get_min_year
import ipinfo


class CarAdStandardPagination(PageNumberPagination):
    page_size = 50
    additional_info = []

    def get_paginated_response(self, data):
        # adding field totalPages to response
        response = super(CarAdStandardPagination, self).get_paginated_response(data)
        response.data['totalPages'] = self.page.paginator.num_pages
        response.data['models'] = self.additional_info
        return response

    def paginate_queryset(self, queryset, request, view=None):
        result = super(CarAdStandardPagination, self).paginate_queryset(queryset, request)
        self.additional_info = get_models_and_count(queryset, request)
        return result


class CarAdViewSet(viewsets.ModelViewSet):
    queryset = CarAdvertisement.objects.all().order_by('-id')
    serializer_class = CarAdSerializer
    pagination_class = CarAdStandardPagination
    filterset_class = CarAdFilter


class MinYearView(APIView):
    def get(self, request, format=None):
        result = {
            "min_year": get_min_year()
        }
        return Response(result)
