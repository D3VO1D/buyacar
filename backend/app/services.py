from django.conf import settings
import ipinfo

from .models import CarAdvertisement
from django.db.models import Count


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
    return CarAdvertisement.objects.values('make').annotate(count=Count('make')).order_by('-count')


def get_ordered_by_distance_queryset(request, queryset):
    ip = get_client_ip(request)
    ip_data = get_ip_details(ip)
    latitude, longitude = float(ip_data.latitude), float(ip_data.longitude)
    sorted_list = sorted(
        queryset, key=lambda x: (latitude - x.latitude) ** 2 + \
                                (longitude - x.longitude) ** 2)
    pk_list = [x.id for x in sorted_list]
    ordering = 'FIELD(`id`, %s)' % ','.join(str(id) for id in pk_list)
    return CarAdvertisement.objects.filter(pk__in=pk_list).extra(
        select={'ordering': ordering}, order_by=('ordering',))


def get_min_year():
    return int(CarAdvertisement.objects.exclude(year=0.0).order_by('year')[0].year)
