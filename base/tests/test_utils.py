import googlemaps

from django.test import TestCase

from base.utils import GeoCoder
from base.models import GeoCoderLog


class GeoCoderTester(TestCase):

    def test_invalid_address(self):
        geocoder = GeoCoder()
        geocoder.geocode('')
        address = geocoder.get_address()

        self.assertEqual(geocoder.has_error(), True)
        self.assertIsInstance(geocoder.get_error(), googlemaps.exceptions.HTTPError)
        self.assertEqual(geocoder.get_error().status_code, 400)
        self.assertEqual(address.is_valid(), False)

    def test_address(self):
        geocoder = GeoCoder()
        geocoder.geocode('Budapest Király utca 46.')
        address = geocoder.get_address()

        self.assertEqual(address.is_valid(), True)
        self.assertEqual(geocoder.has_error(), False)
        self.assertEqual(address.street_number, '46')
        self.assertEqual(address.postal_code, '1061')
        self.assertEqual(address.locality, 'Budapest')
        self.assertEqual(address.route, 'Király utca')
        self.assertEqual(address.formatted_address, 'Budapest, Király u. 46, 1061 Hungary')
