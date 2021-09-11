from django_filters import rest_framework as filters
from .models import CarAdvertisement


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
    price_from = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_to = filters.NumberFilter(field_name="price", lookup_expr='lte')
    year_from = filters.NumberFilter(field_name="year", lookup_expr='gte')
    year_to = filters.NumberFilter(field_name="year", lookup_expr='lte')
    mileage_from = filters.NumberFilter(field_name="year", lookup_expr='gte')
    mileage_to = filters.NumberFilter(field_name="year", lookup_expr='lte')
    drive = filters.ChoiceFilter(choices=DRIVE_CHOICES)
    transmission = filters.ChoiceFilter(choices=TRANSMISSION_CHOICES)
    body = filters.ChoiceFilter(choices=BODY_CHOICES)
    only_with_photos = filters.BooleanFilter(field_name="photos", method="has_photos", label="Only with photos")

    def has_photos(self, queryset, name, value):
        # Checks if "http" in photos. Works with our data, maybe needs to rethink
        return queryset.filter(photos__icontains='http') if value else queryset

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            data.setdefault("is_broken", False)
            data.setdefault("only_with_photos", False)
        super(CarAdFilter, self).__init__(data, *args, **kwargs)

    class Meta:
        model = CarAdvertisement
        fields = ['is_new', 'is_broken', 'price_from', 'price_to', 'year_from', 'year_to',
                  'make', 'model', 'mileage_from', 'mileage_to', 'drive', 'transmission',
                  'body', 'only_with_photos']
