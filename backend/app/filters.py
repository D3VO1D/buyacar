from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from django.db.models import FloatField, Value

from .models import CarAdvertisement
from .services import get_ip_details, get_client_ip, get_locations_nearby_coords

import logging
logger = logging.getLogger(__name__)


DRIVE_CHOICES = (
    ("AWD", "AWD"),
    ("RWD", "RWD"),
    ("FWD", "FWD"),
)

TRANSMISSION_CHOICES = (
    ("Automatic", "Automatic"),
    ("Manual", "Manual"),
)

BODY_CHOICES = (
    ("Hatchback", "Hatchback"),
    ("Coupe", "Coupe"),
    ("Convertible", "Convertible"),
    ("Sedan", "Sedan"),
    ("SUV", "SUV"),
    ("Pickup Truck", "Pickup Truck"),
    ("Commercial", "Commercial"),
    ("Minivan", "Minivan"),
    ("Wagon", "Wagon"),
)


class CarAdFilter(filters.FilterSet):
    """
    Filter not considering city and distance
    """
    price_from = filters.NumberFilter(field_name="price", method="price_from_exclude_zero")
    price_to = filters.NumberFilter(field_name="price", method="price_to_exclude_zero")
    year_from = filters.NumberFilter(field_name="year", lookup_expr='gte')
    year_to = filters.NumberFilter(field_name="year", lookup_expr='lte')
    mileage_from = filters.NumberFilter(field_name="mileage", lookup_expr='gte')
    mileage_to = filters.NumberFilter(field_name="mileage", lookup_expr='lte')
    drive = filters.MultipleChoiceFilter(choices=DRIVE_CHOICES)
    transmission = filters.ChoiceFilter(choices=TRANSMISSION_CHOICES)
    body = filters.MultipleChoiceFilter(choices=BODY_CHOICES)
    only_with_photo = filters.BooleanFilter(field_name="photos", method="has_photos", label="Only with photo")

    def price_from_exclude_zero(self, queryset, name, value):
        # filters price from the value, excluding zero
        return queryset.exclude(price=0).filter(price__gte=value)

    def price_to_exclude_zero(self, queryset, name, value):
        # filters price to the value, excluding zero
        return queryset.exclude(price=0).filter(price__lte=value)

    def has_photos(self, queryset, name, value):
        # Excludes objects without photos for only_with_photos field
        return queryset.exclude(photos__exact='[]') if value else queryset

    class Meta:
        model = CarAdvertisement
        fields = ['is_new', 'is_broken', 'make', 'model']


class DistanceOrderingFilter(OrderingFilter):
    """
    Order queryset by given params or by distance
    and filter by city
    """

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)

        request_latitude = request.query_params.get('latitude', None)
        request_longitude = request.query_params.get('longitude', None)
        request_city = request.query_params.get('location', None)
        distance = request.query_params.get('distance', None)

        if request_latitude and request_longitude and request_city:
            latitude, longitude, city = request_latitude, request_longitude, request_city.split(',')[0]
        else:
            ip_data = get_ip_details(get_client_ip(request))
            latitude, longitude, city = ip_data.latitude, ip_data.longitude, ip_data.city

        logger.info('{} {}'.format(city, request.META['QUERY_STRING']))
        queryset = get_locations_nearby_coords(queryset, latitude, longitude, distance, city)
        if not ordering:
            queryset = queryset.order_by("distance")
        else:
            if "price" in ordering[0]:  # ordering is a list
                queryset = queryset.exclude(price=0)
            queryset = super(DistanceOrderingFilter, self).filter_queryset(request, queryset, view)

        return queryset
