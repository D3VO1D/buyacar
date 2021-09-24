from http import HTTPStatus
from django.test import TestCase, RequestFactory

from django.core.management import call_command
from app.models import CarAdvertisement
from app.views import CarAdViewSet, CarMakesView, UserCityView, MinYearView
from app.services import get_distance_between_coords


class AdditionalViewsTest(TestCase):
    """
    Test all views except CarAdViewSet
    """
    def setUp(self):
        # creates test db from backend/ads.csv if it doesn't exist yet, then deletes it
        self.factory = RequestFactory()
        if not CarAdvertisement.objects.exists():
            call_command("generate_database", '--num_rows=50', '--num_photos=5')

    def test_car_makes_view(self):
        """
        Test CarMakesView
        """
        request = self.factory.get('/api/v1/makes')
        response = CarMakesView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        # Checks if first make is lower than the second by alphabet order
        self.assertLess(response.data[0]['make'].lower(), response.data[1]['make'].lower())

    def test_user_city_view(self):
        """
        Test UserViewCity
        """
        request = self.factory.get('/api/v1/usercity')
        response = UserCityView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        # city and region must be string
        self.assertIs(type(response.data['city']), str)
        self.assertIs(type(response.data['region']), str)

    def test_min_year_view(self):
        """
        Test MinYearView
        """
        request = self.factory.get('/api/v1/usercity')
        response = MinYearView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        # minimum year must be greater than 0 and must be integer
        self.assertIs(type(response.data['min_year']), int)
        self.assertGreater(response.data['min_year'], 0)


class CarAdViewSetTest(TestCase):
    latitude = 25.77427
    longitude = -80.19366
    location = 'Miami, FL'

    def setUp(self):
        self.factory = RequestFactory()
        if not CarAdvertisement.objects.exists():
            call_command("generate_database", '--num_rows=50', '--num_photos=5')

    def test_default_ordering(self):
        """
        Test if first site opening works
        """
        request = self.factory.get('/api/v1/cars', {'latitude': self.latitude,
                                                    'longitude': self.longitude,
                                                    'location': self.location,
                                                    'distance': 10000})  # inf distance to show all ads
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        # find two nearest cars and distance from our location to them
        cars = response.data['results'][0:2]
        d = [get_distance_between_coords(self.latitude,
                                         self.longitude,
                                         cars[i]['latitude'],
                                         cars[i]['longitude']
                                         ) for i in range(2)]
        # the first car must be closer than the second one
        self.assertLessEqual(d[0], d[1])
        # and they must not be similar
        self.assertNotEqual(cars[0], cars[1])

    def test_ordering_by_price_desc(self):
        """
        Test if ordering by price descending works
        """
        request = self.factory.get('/api/v1/cars', {'distance': 10000,
                                                    'ordering': '-price'})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        cars = response.data['results'][0:2]
        self.assertGreater(cars[0]['price'], cars[1]['price'])
        self.assertNotEqual(cars[0], cars[1])

    def test_filter_drive_AWD(self):
        """
        Test if drive choice filter work. The same for body and transmission
        """
        request = self.factory.get('/api/v1/cars', {'distance': 10000,
                                                    'drive': 'AWD'})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        car_without_awd = None
        for car in response.data['results']:
            if car['drive'] != "AWD":
                car_without_awd = car
                break
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        self.assertIs(car_without_awd, None)

    def test_filter_mileage_between(self):
        """
        Test if integer input mileage filter works. The same for price and year
        """
        request = self.factory.get('/api/v1/cars', {'mileage_from': 1000,
                                                    'mileage_to': 100000,
                                                    'distance': 10000})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        car_in_mileage = None
        for car in response.data['results']:
            if not 1000 < car['mileage'] < 100000:
                car_in_mileage = car
                break
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        self.assertIs(car_in_mileage, None)

    def test_filter_only_with_photo(self):
        """
        Test if checkbox only_with_photo filter works
        """
        request = self.factory.get('/api/v1/cars', {'only_with_photo': True,
                                                    'distance': 1000})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        car_without_photo = None
        for car in response.data['results']:
            if not car['photos']:
                car_without_photo = car
                break
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        self.assertIs(car_without_photo, None)

    def test_filter_make_and_model(self):
        """
        Test if string input filter for make and model works
        """
        request = self.factory.get('/api/v1/cars', {'make': 'BMW',
                                                    'model': '3 Series',
                                                    'distance': 100000})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        car_other_make = None
        for car in response.data['results']:
            if car['make'] != 'BMW' or car['model'] != '3 Series':
                car_other_make = car
                break
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        self.assertIs(car_other_make, None)

    def test_get_models_by_make(self):
        """
        Test if it shows models if make is chosen
        """
        request = self.factory.get('/api/v1/cars', {'make': 'BMW',
                                                    'distance': 100000})
        response = CarAdViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        self.assertNotEqual(response.data['models'], [])
        self.assertIs(type(response.data['models'][0]['model']), str)
        self.assertIs(type(response.data['models'][0]['count']), int)
