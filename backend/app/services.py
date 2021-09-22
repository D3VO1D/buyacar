from django.conf import settings
from collections import Counter
import ipinfo
from django.db.models.expressions import RawSQL

from .models import CarAdvertisement
from django.db.models import Count

MILES_PER_LONG = 54.6
MILES_PER_LAT = 69


def string_to_json_array(string, max_len_of_array):
    array = string[1:-1].split(', ')
    clipped_array = array[0:max_len_of_array] \
        if len(array) > max_len_of_array else array[0:len(array)]
    for i in range(len(clipped_array)):
        clipped_array[i] = clipped_array[i].replace("\"", "")
    return clipped_array if clipped_array != [""] else []


def get_ip_details(ip_address=None):
    ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
    ipinfo_settings = getattr(settings, "IPINFO_SETTINGS", {})
    ip_data = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
    ip_data = ip_data.getDetails(ip_address)
    return ip_data


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if ip.startswith("192.168.") or ip == "127.0.0.1":
        return "168.156.54.5"
    return ip


def get_client_city_region_as_json(request):
    ip_details = get_ip_details(get_client_ip(request))
    result = {
        'city': ip_details.city,
        'region': ip_details.region
    }
    return result


def get_models_and_count(queryset, request):
    # if make is chosen, it has to show the models and their count
    if request.query_params.get("make", None):
        return queryset.values('model').annotate(count=Count('model')).order_by('-count')
    return []


def get_makes_and_count(request):
    query = """
        SELECT 1 as id, make 
        FROM ( 
            SELECT make, count(*) counter 
            FROM ads
            WHERE make <> '' 
            GROUP BY make 
            ORDER BY counter 
            desc LIMIT 50 
            ) m 
        ORDER BY make asc
    """
    return CarAdvertisement.objects.raw(query)

def get_min_year():
    return int(CarAdvertisement.objects.exclude(year=0.0).order_by('year')[0].year)


def get_locations_nearby_coords(latitude, longitude, queryset, max_distance, city):
    """
    Return objects sorted by distance to specified coordinates
    which distance is less than max_distance given in kilometers
    """
    # Great circle distance formula in miles
    gcd_formula = "3440 * acos(least(greatest(\
    cos(radians(%s)) * cos(radians(latitude)) \
    * cos(radians(longitude) - radians(%s)) + \
    sin(radians(%s)) * sin(radians(latitude)) \
    , -1), 1))"
    distance_raw_sql = RawSQL(
        gcd_formula,
        (latitude, longitude, latitude)
    )
    qs1 = queryset.annotate(distance=distance_raw_sql)
    if max_distance is not None:
        qs1 = qs1.filter(distance__lt=max_distance)
    qs2 = queryset.filter(location__icontains=city).annotate(distance=distance_raw_sql)
    qs = qs1 | qs2
    return qs
