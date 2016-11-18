from django.test import TestCase

from crm.validators import (
    validate_address,
    validate_phone,
    validate_email
)


class ValidateAddressTester(TestCase):

    def test_invalid_address(self):
        address = validate_address({
            'locality': '',
            'postal_code': '',
            'route': '',
            'street_number': '',
            'country': ''
        })

        self.assertEqual(address['is_valid'], False)
        self.assertEqual(address['locality'], '')
        self.assertEqual(address['postal_code'], '')

    def test_valid_address(self):
        address = validate_address({
            'locality': 'Budapest',
            'postal_code': '1061',
            'route': 'Király utca',
            'street_number': '46',
            'country': 'Hungary'
        })

        self.assertEqual(address['is_valid'], True)
        self.assertEqual(address['formatted_address'], 'Budapest, Király u. 46, 1061 Hungary')


class ValidatePhoneTester(TestCase):

    def test_invalid_phone(self):
        phone = validate_phone({'number': '123', 'country': 'HU'})

        self.assertEqual(phone['is_valid'], False)

    def test_valid_phone(self):
        phone = validate_phone({'number': '06706712235', 'country': 'HU'})

        self.assertEqual(phone['is_valid'], True)


class ValidateEmailTester(TestCase):

    def test_invalid_email(self):
        email = validate_email({'email': 'test'})

        self.assertEqual(email['is_valid'], False)

    def test_valid_email(self):
        email = validate_email({'email': 'test@test.com'})

        self.assertEqual(email['is_valid'], True)
