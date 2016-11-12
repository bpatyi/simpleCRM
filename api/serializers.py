import phonenumbers

from crm.models import (
    Individual,
    IndividualAddress,
    IndividualPhone,
    IndividualEmail,
    InboundContact,
    InboundContactEmail,
    InboundContactPhone,
    InboundContactAddress,
    OutboundContact,
    OutboundContactMailInfo,
    OutboundContactEmailInfo,
    OutboundContactPhoneInfo,
    Campaign,
    SourceType,
    Source
)
from crm.validators import (
    validate_address,
    validate_phone,
    validate_email
)

from rest_framework import serializers


class IndividualAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualAddress
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'final_type',
            'formatted_address',
            'latitude',
            'longitude',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_address(validated_data)


class IndividualPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualPhone
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'type',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_phone(validated_data)


class IndividualEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualEmail
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_email(validated_data)


class IndividualSerializer(serializers.ModelSerializer):
    address = IndividualAddressSerializer(many=True)
    phones = IndividualPhoneSerializer(many=True)
    emails = IndividualEmailSerializer(many=True)

    class Meta:
        model = Individual
        fields = [
            'gender',
            'title',
            'first_name',
            'last_name',
            'family_status',
            'education_level',
            'birth_date',
            'address',
            'phones',
            'emails'
        ],
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        phones_data = validated_data.pop('phones')
        emails_data = validated_data.pop('emails')

        individual = Individual.objects.create(**validated_data)

        if address_data:
            IndividualAddress.objects.create(individual=individual, **address_data)

        for phone in phones_data:
            IndividualPhone.objects.create(individual=individual, **phone)

        for email in emails_data:
            IndividualEmail.objects.create(individual=individual, **email)

        return individual


class InboundContactAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactAddress
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'final_type',
            'formatted_address',
            'latitude',
            'longitude',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_address(validated_data)


class InboundContactPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactPhone
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'type',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_phone(validated_data)


class InboundContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactEmail
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'created_at',
            'updated_at'
        ]

    def validate(self, validated_data):
        return validate_email(validated_data)


class InboundContactSerializer(serializers.ModelSerializer):
    address = InboundContactAddressSerializer(many=True)
    phones = InboundContactPhoneSerializer(many=True)
    emails = InboundContactEmailSerializer(many=True)

    class Meta:
        model = InboundContact
        fields = [
            'gender',
            'title',
            'first_name',
            'last_name',
            'family_status',
            'education_level',
            'birth_date',
            'address',
            'phones',
            'emails'
        ]
        read_only_fields = [
            'id',
            'is_valid',
            'is_cleansed',
            'created_at',
            'updated_at'
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        phones_data = validated_data.pop('phones')
        emails_data = validated_data.pop('emails')

        inbound_contact = InboundContact.objects.create(**validated_data)

        if address_data:
            InboundContactAddress.objects.create(inbound_contact=inbound_contact, **address_data)

        for phone in phones_data:
            InboundContactPhone.objects.create(inbound_contact=inbound_contact, **phone)

        for email in emails_data:
            InboundContactEmail.objects.create(inbound_contact=inbound_contact, **email)

        return inbound_contact


class OutboundContactMailInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutboundContactMailInfo
        fields = '__all__'


class OutboundContactEmailInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutboundContactEmailInfo
        fields = '__all__'
        read_only_fields = [
            'id',
            'is_soft_bounced',
            'is_hard_bounced',
            'created_at',
            'updated_at'
        ]


class OutboundContactPhoneInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutboundContactPhoneInfo
        fields = '__all__'


class OutboundContactSerializer(serializers.ModelSerializer):
    mail_info = OutboundContactMailInfoSerializer(many=True)
    phone_infos = OutboundContactPhoneInfoSerializer(many=True)
    email_infos = OutboundContactEmailInfoSerializer(many=True)

    class Meta:
        model = OutboundContact
        fields = '__all__'

    def create(self, validated_data):
        mail_info = validated_data.pop('mail_info')
        phone_infos = validated_data.pop('phone_infos')
        email_infos = validated_data.pop('email_infos')

        outbound_contact = OutboundContact.objects.create(**validated_data)

        if mail_info:
            OutboundContactMailInfo.objects.create(outbound_contact=outbound_contact, **mail_info)

        for phone_info in phone_infos:
            OutboundContactPhoneInfo.objects.create(outbound_contact=outbound_contact, **phone_info)

        for email_info in email_infos:
            OutboundContactEmailInfo.objects.create(outbound_contact=outbound_contact, **email_info)

        return outbound_contact


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'


class SourceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceType
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = '__all__'
