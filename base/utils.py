import googlemaps

from django.conf import settings

from base.models import GeoCoderLog

client = googlemaps.Client(key=settings.GOOGLE_MAP_KEY)


class GoogleAddress(object):

    def __init__(self):
        self.country = None
        self.postal_code = None
        self.postal_code_suffix = None
        self.county = None
        self.administrative_area = None
        self.locality = None
        self.district = None
        self.route = None
        self.street_number = None
        self.type = None
        self.formatted_address = None
        self.latitude = None
        self.longitude = None

        self.is_valid = False
        self.is_cleansed = False

    def process_response(self, response):
        if not response:
            return

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
        self.is_cleansed = True

        return self

    def is_valid(self):
        return self.is_valid


class GeoCoder(object):

    def __init__(self):
        self.__google_address = GoogleAddress()
        self.__error = None

    def geocode(self, address):

        if GeoCoderLog.get_limit() == 0:
            self.error = 'You used all your google maps option.'
            return

        try:
            GeoCoderLog.update_today_number_of_request()
            response = client.geocode(address)
        except googlemaps.exceptions.HTTPError as e:
            self.__error = e
            return
        except googlemaps.exceptions.ApiError as e:
            self.__error = e
            return
        except googlemaps.exceptions.TransportError as e:
            self.__error = e
            return
        except googlemaps.exceptions.Timeout as e:
            self.__error = e
            return

        self.__google_address.process_response(response)

    def get_address(self):
        return self.__google_address

    def has_error(self):
        return self.__error is not None

    def get_error(self):
        return self.__error
