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


class InboundContactTester(TestCase):

    def setUp(self):
        self.individual = Individual.objects.create(
            gender='M',
            title='dr',
            first_name='Joe',
            last_name='Don',
            family_status='S',
            education_level='E'
        )
        self.source_type = SourceType.objects.create(
            name="Test Source Type"
        )
        self.source = Source.objects.create(
            name="Test Source",
            type_of_source=self.source_type
        )

        self.inbound_contact = InboundContact.objects.create(
            individual=self.individual,
            gender='M',
            title='dr',
            first_name='Joe',
            last_name='Don',
            family_status='S',
            education_level='E',
            source=self.source,
            searchable_channels=['M', 'E', 'P']
        )

    def test_inbound_contact(self):
        self.assertIsInstance(self.inbound_contact, InboundContact)
        self.assertIsInstance(self.individual, Individual)
        self.assertIsInstance(self.source, Source)
        self.assertIsInstance(self.source_type, SourceType)

        self.assertEqual(self.inbound_contact.individual.id, self.individual.id)
        self.assertEqual(self.inbound_contact.source.id, self.source.id)
        self.assertEqual(self.inbound_contact.source.type_of_source.id, self.source_type.id)

        self.assertEqual(self.inbound_contact.gender, 'M')
        self.assertEqual(self.inbound_contact.title, 'dr')
        self.assertEqual(self.inbound_contact.first_name, 'Joe')
        self.assertEqual(self.inbound_contact.last_name, 'Don')
        self.assertEqual(self.inbound_contact.family_status, 'S')
        self.assertEqual(self.inbound_contact.education_level, 'E')
        self.assertEqual(self.inbound_contact.searchable_channels, ['M', 'E', 'P'])

    def test_inbound_contact_address(self):
        address = InboundContactAddress.objects.create(
            inbound_contact=self.inbound_contact,
            country='HU',
            postal_code='1061',
            county='Budapest',
            locality='Budapest',
            route='Király utca',
            street_number='46',
            formatted_address='Budapest, Király u. 46, 1061 Hungary'
        )

        self.assertIsInstance(address, InboundContactAddress)
        self.assertEqual(address.inbound_contact.id, self.inbound_contact.id)
        self.assertEqual(address.country, 'HU')
        self.assertEqual(address.postal_code, '1061')
        self.assertEqual(address.county, 'Budapest')
        self.assertEqual(address.locality, 'Budapest')
        self.assertEqual(address.route, 'Király utca')
        self.assertEqual(address.street_number, '46')
        self.assertEqual(address.formatted_address, 'Budapest, Király u. 46, 1061 Hungary')

    def test_inbound_contact_phone(self):
        phone = InboundContactPhone.objects.create(
            inbound_contact=self.inbound_contact,
            country='HU',
            number='+36701234567',
            type='mobile'
        )

        self.assertIsInstance(phone, InboundContactPhone)
        self.assertEqual(phone.inbound_contact.id, self.inbound_contact.id)
        self.assertEqual(phone.country, 'HU')
        self.assertEqual(phone.number, '+36701234567')
        self.assertEqual(phone.type, 'mobile')

    def test_inbound_contact_email(self):
        email = InboundContactEmail.objects.create(
            inbound_contact=self.inbound_contact,
            email='joe.don@test.com'
        )

        self.assertIsInstance(email, InboundContactEmail)
        self.assertEqual(email.inbound_contact.id, self.inbound_contact.id)
        self.assertEqual(email.email, 'joe.don@test.com')


class OutboundContactTester(TestCase):

    def setUp(self):
        self.individual = Individual.objects.create(
            gender='M',
            title='dr',
            first_name='Joe',
            last_name='Don',
            family_status='S',
            education_level='E'
        )
        self.campaign = Campaign.objects.create(
            name="Test Campaign",
            start_date="2015-01-01",
            end_date="2015-12-01"
        )
        self.outbound_contact = OutboundContact.objects.create(
            individual=self.individual,
            campaign=self.campaign,
            contact_type='E',
            date_of_contact="2015-10-20",
            is_success=True
        )
        self.address = IndividualAddress.objects.create(
            individual=self.individual,
            country='HU',
            postal_code='1061',
            county='Budapest',
            locality='Budapest',
            route='Király utca',
            street_number='46',
            formatted_address='Budapest, Király u. 46, 1061 Hungary'
        )
        self.email = IndividualEmail.objects.create(
            individual=self.individual,
            email='joe.don@test.com'
        )
        self.phone = IndividualPhone.objects.create(
            individual=self.individual,
            country='HU',
            number='+36701234567',
            type='mobile'
        )

    def test_outbound_contact(self):
        self.assertIsInstance(self.outbound_contact, OutboundContact)
        self.assertIsInstance(self.campaign, Campaign)
        self.assertIsInstance(self.individual, Individual)

        self.assertEqual(self.outbound_contact.individual.id, self.individual.id)
        self.assertEqual(self.outbound_contact.campaign.id, self.campaign.id)
        self.assertEqual(self.outbound_contact.contact_type, 'E')
        self.assertEqual(self.outbound_contact.date_of_contact, "2015-10-20")
        self.assertEqual(self.outbound_contact.is_success, True)

    def test_outbound_contact_mail_info(self):
        mail_info = OutboundContactMailInfo.objects.create(
            outbound_contact=self.outbound_contact,
            address=self.address,
            is_deliverable=False
        )

        self.assertIsInstance(mail_info, OutboundContactMailInfo)
        self.assertEqual(mail_info.outbound_contact.id, self.outbound_contact.id)
        self.assertEqual(mail_info.address, self.address)
        self.assertEqual(mail_info.is_deliverable, False)

    def test_outbound_contact_phone_info(self):
        phone_info = OutboundContactPhoneInfo.objects.create(
            outbound_contact=self.outbound_contact,
            phone=self.phone,
            is_available=True,
            call_times=[
                '2015-10-15 13:35:36',
                '2015-11-12 10:25:56',
                '2015-04-23 09:55:16'
            ],
            success_call_times=[
                '2015-11-12 10:25:56'
            ]
        )

        self.assertIsInstance(phone_info, OutboundContactPhoneInfo)
        self.assertEqual(phone_info.outbound_contact.id, self.outbound_contact.id)
        self.assertEqual(phone_info.phone, self.phone)
        self.assertEqual(phone_info.is_available, True)
        self.assertEqual(phone_info.call_times, ['2015-10-15 13:35:36', '2015-11-12 10:25:56', '2015-04-23 09:55:16'])
        self.assertEqual(phone_info.success_call_times, ['2015-11-12 10:25:56'])

    def test_outbound_contact_email_info(self):
        email_info = OutboundContactEmailInfo.objects.create(
            outbound_contact=self.outbound_contact,
            email=self.email,
            is_unsubscribed=False,
            number_of_bounced=3,
            open_times=[
                '2015-06-06 12:15:51',
                '2015-08-06 09:35:56'
            ],
            clicked_links=[
                'https://www.test.com'
            ]
        )

        self.assertIsInstance(email_info, OutboundContactEmailInfo)
        self.assertEqual(email_info.outbound_contact.id, self.outbound_contact.id)
        self.assertEqual(email_info.email, self.email)
        self.assertEqual(email_info.is_unsubscribed, False)
        self.assertEqual(email_info.number_of_bounced, 3)
        self.assertEqual(email_info.is_soft_bounced, True)
        self.assertEqual(email_info.is_hard_bounced, False)
        self.assertEqual(email_info.open_times, ['2015-06-06 12:15:51', '2015-08-06 09:35:56'])
        self.assertEqual(email_info.clicked_links, ['https://www.test.com'])
        self.assertEqual(email_info.is_opened, True)
        self.assertEqual(email_info.is_clicked, True)


class CampaignTester(TestCase):

    def test_campaign(self):
        campaign = Campaign.objects.create(
            name="Test Campaign",
            start_date="2015-01-01",
            end_date="2015-12-30"
        )

        self.assertIsInstance(campaign, Campaign)
        self.assertEqual(campaign.name, "Test Campaign")
        self.assertEqual(campaign.start_date, "2015-01-01")
        self.assertEqual(campaign.end_date, "2015-12-30")
