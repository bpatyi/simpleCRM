import os
import googlemaps

from django.conf import settings


client = googlemaps.Client(key=settings.GOOGLE_MAP_KEY)


class GeoCoder(object):

    @staticmethod
    def geocode(address):
        return GoogleAddress(address)


class GoogleAddress(object):
    country = None
    postal_code = None
    postal_code_suffix = None
    county = None
    administrative_area = None
    locality = None
    district = None
    route = None
    street_number = None
    type = None
    formatted_address = None
    latitude = None
    longitude = None

    is_valid = False

    def __init__(self, address):
        response = client.geocode(address)

        if not response:
            return

        self.process_response(response)

    def process_response(self, response):
        data = response[0]
        address_components = data.get('address_components')

        for component in address_components:
            types = component.get('types')
            value = component.get('long_name')

            if 'street_number' in types:
                self.street_number = value
            elif 'route' in types:
                self.route = value
            elif 'sublocality' in types:
                self.district = value
            elif 'locality' in types:
                self.locality = value
            elif 'country' in types:
                self.country = component.get('short_name')
            elif 'postal_code' in types:
                self.postal_code = value
            elif 'postal_code_suffix' in types:
                self.postal_code_suffix = value
            elif 'administrative_area_level_1' in types:
                self.county = value
            elif 'administrative_area_level_2' in types:
                self.administrative_area = value

        self.formatted_address = data.get('formatted_address')
        self.latitude = data['geometry']['location'].get('lat')
        self.longitude = data['geometry']['location'].get('lng')
        self.type = data['types'][0]

        self.is_valid = True

    def is_valid_address(self):
        return self.is_valid
