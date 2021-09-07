from django.core.management.base import BaseCommand
import pandas as pd

from app.models import CarAdvertisement
from app.services import string_to_json_array


class Command(BaseCommand):
    help = """Database generation from backend/ads.csv Try running: 
              python manage.py generate_database --num_rows=100 --num_photos=5 or 
              python manage.py generate_database --num_photos=5"""

    def add_arguments(self, parser):
        parser.add_argument("--num_rows", type=int, help="Number of rows called from csv")
        parser.add_argument("--num_photos", type=int, help="Maximum number of photos for ad")

    def handle(self, *args, **kwargs):
        try:
            num_rows = kwargs['num_rows']
            cars = pd.read_csv("ads.csv", nrows=num_rows, delimiter=";")
        except:
            cars = pd.read_csv("ads.csv", delimiter=";")

        num_photos = kwargs['num_photos']

        for index, car in cars.iterrows():
            if car.make == "nan" and car.model == "nan":
                continue
            new_car_ad = CarAdvertisement.objects.create(source=car.source,
                                                         url=car.url,
                                                         is_new=True if car.is_new == "1" else False,
                                                         is_broken=car.is_broken,
                                                         price=car.price,
                                                         location=car.location,
                                                         latitude=car.latitude,
                                                         longitude=car.longitude,
                                                         photos=string_to_json_array(car.photos, num_photos),
                                                         title=car.title,
                                                         make=car.make,
                                                         model=car.model,
                                                         year=car.year,
                                                         body=car.body,
                                                         vin=car.vin,
                                                         mileage=car.mileage,
                                                         transmission=car.transmission,
                                                         drive=car.drive,
                                                         power=car.power
                                                         )
