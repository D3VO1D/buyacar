from django.conf import settings
from collections import Counter
import ipinfo

from .models import CarAdvertisement


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


def get_models_and_count(queryset, request):
    # if make is chosen, it has to show the models and their count
    if request.query_params.get("make", None):
        c = Counter(queryset.values_list("model"))  # count('year').distinct() doesn't work here
        return sorted([{'model': i[0], 'count': c[i]} for i in c],
                      key=lambda x: -x["count"])
    return []


def get_min_year():
    return int(CarAdvertisement.objects.exclude(year=0.0).order_by('year')[0].year)
