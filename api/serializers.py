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

from rest_framework import serializers


class IndividualAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualAddress
        fields = '__all__'


class IndividualPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualPhone
        fields = '__all__'


class IndividualEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualEmail
        fields = '__all__'


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


class InboundContactPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactPhone
        fields = '__all__'


class InboundContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactEmail
        fields = '__all__'


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

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        phones_data = validated_data.pop('phones')
        emails_data = validated_data.pop('emails')

        inbound_contact = InboundContact.objects.create(**validated_data)

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
