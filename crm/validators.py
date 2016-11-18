import phonenumbers

from django.core.exceptions import ValidationError
from django.core.validators import validate_email as dj_validate_email

from base.utils import GeoCoder
from crm.models import IndividualPhone


def validate_address(data):
    address = ' '.join([
        data.get('locality'),
        data.get('route'),
        str(data.get('street_number', '')),
        data.get('postal_code'),
        data.get('country')
    ])

    geocoder = GeoCoder()
    geocoder.geocode(address)
    address = geocoder.get_address()

    if geocoder.has_error():
        data['is_valid'] = False
        data['is_cleansed'] = False
        return data
    elif not address.is_valid():
        data['is_valid'] = False
        data['is_cleansed'] = True
        return data

    return address.__dict__


def validate_phone(data):
    data['is_valid'] = False
    data['is_cleansed'] = False

    try:
        number = phonenumbers.parse(data.get('number'), data.get('country'))
    except phonenumbers.NumberParseException:
        return data

    if not phonenumbers.is_valid_number(number):
        return data

    data['number'] = phonenumbers.format_number(
        number,
        phonenumbers.PhoneNumberFormat.E164
    )

    data['type'] = IndividualPhone.get_type(
        phonenumbers.number_type(number)
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
