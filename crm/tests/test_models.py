from django.test import TestCase

from crm.models import (
    Individual,
    IndividualAddress,
    IndividualEmail,
    IndividualPhone,
    InboundContact,
    InboundContactAddress,
    InboundContactEmail,
    InboundContactPhone,
    OutboundContact,
    OutboundContactEmailInfo,
    OutboundContactPhoneInfo,
    OutboundContactMailInfo,
    Campaign,
    Source,
    SourceType
)


class IndividualTester(TestCase):

    def setUp(self):
        self.individual = None
        self.individual = Individual.objects.create(
            gender='M',
            title='dr',
            first_name='Joe',
            last_name='Don',
            family_status='S',
            education_level='E'
        )

    def test_individual(self):
        self.assertIsInstance(self.individual, Individual)
        self.assertEqual(self.individual.gender, 'M')
        self.assertEqual(self.individual.title, 'dr')
        self.assertEqual(self.individual.first_name, 'Joe')
        self.assertEqual(self.individual.last_name, 'Don')
        self.assertEqual(self.individual.family_status, 'S')
        self.assertEqual(self.individual.education_level, 'E')
        self.assertEqual(str(self.individual), 'dr Joe Don')
        self.assertEqual(self.individual.get_full_name(), 'dr Joe Don')

    def test_individual_address(self):
        address = IndividualAddress.objects.create(
            individual=self.individual,
            country='HU',
            postal_code='1061',
            county='Budapest',
            locality='Budapest',
            route='Király utca',
            street_number='46',
            formatted_address='Budapest, Király u. 46, 1061 Hungary'
        )

        self.assertIsInstance(address, IndividualAddress)
        self.assertEqual(address.individual.id, self.individual.id)
        self.assertEqual(address.country, 'HU')
        self.assertEqual(address.postal_code, '1061')
        self.assertEqual(address.county, 'Budapest')
        self.assertEqual(address.locality, 'Budapest')
        self.assertEqual(address.route, 'Király utca')
        self.assertEqual(address.street_number, '46')
        self.assertEqual(address.formatted_address, 'Budapest, Király u. 46, 1061 Hungary')

    def test_individual_phone(self):
        phone = IndividualPhone.objects.create(
            individual=self.individual,
            country='HU',
            number='+36701234567',
            type='mobile'
        )

        self.assertIsInstance(phone, IndividualPhone)
        self.assertEqual(phone.individual.id, self.individual.id)
        self.assertEqual(phone.country, 'HU')
        self.assertEqual(phone.number, '+36701234567')
        self.assertEqual(phone.type, 'mobile')

    def test_individual_email(self):
        email = IndividualEmail.objects.create(
            individual=self.individual,
            email='joe.don@test.com'
        )

        self.assertIsInstance(email, IndividualEmail)
        self.assertEqual(email.individual.id, self.individual.id)
        self.assertEqual(email.email, 'joe.don@test.com')
        
