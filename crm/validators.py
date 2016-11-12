import phonenumbers

from django.core.exceptions import ValidationError
from django.core.validators import validate_email as dj_validate_email

from base.utils import GeoCoder
from base.models import GeoCoderLog
from crm.models import IndividualPhone


def validate_address(data):
    if GeoCoderLog.get_limit() == 0:
        data['is_valid'] = False
        data['is_cleansed'] = False
        return data

    address = ' '.join([
        data.get('locality'),
        data.get('route'),
        str(data.get('street_number')),
        data.get('postal_code'),
        data.get('country')
    ])

    geocode = GeoCoder.geocode(address)
    GeoCoderLog.update_today_number_of_request()

    if geocode.is_valid_address():
        data['country'] = geocode.country
        data['postal_code'] = geocode.postal_code
        data['postal_code_suffix'] = geocode.postal_code_suffix
        data['county'] = geocode.county
        data['administrative_area'] = geocode.administrative_area
        data['locality'] = geocode.locality
        data['district'] = geocode.district
        data['route'] = geocode.route
        data['street_number'] = geocode.street_number
        data['final_type'] = geocode.type
        data['formatted_address'] = geocode.formatted_address
        data['latitude'] = geocode.latitude
        data['longitude'] = geocode.longitude

        data['is_valid'] = True

    data['is_cleansed'] = True

    return data


def validate_phone(data):
    try:
        number = phonenumbers.parse(data.get('number'), data.get('country'))
    except phonenumbers.NumberParseException:
        data['is_valid'] = False
        data['is_cleansed'] = False
        return data

    if not phonenumbers.is_valid_number(number):
        data['is_valid'] = False
        data['is_cleansed'] = False
        return data

    data['number'] = phonenumbers.format_number(
        number,
        phonenumbers.PhoneNumberFormat.E164
    )

    data['type'] = IndividualPhone.get_type(
        phonenumbers.number_type(data.get('number'))
    )
    data['is_valid'] = True
    data['is_cleansed'] = True

    return data


def validate_email(data):
    try:
        dj_validate_email(data.get('email'))
    except ValidationError as error:
        data['is_valid'] = False
        data['is_cleansed'] = False
        return data

    data['is_valid'] = True
    data['is_cleansed'] = True

    return data
