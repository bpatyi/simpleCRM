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
    Campaign,
    SourceType,
    Source
)


from rest_framework import serializers


class IndividualAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualAddress


class IndividualPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualPhone


class IndividualEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndividualEmail


class IndividualSerializer(serializers.ModelSerializer):
    address = IndividualAddressSerializer()
    phones = IndividualPhoneSerializer(many=True)
    emails = IndividualEmailSerializer(many=True)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        phones_data = validated_data.pop('phones')
        emails_data = validated_data.pop('emails')

        individual = Individual.objects.create(**validated_data)

        IndividualAddress.objects.create(individual=individual, **address_data)

        for phone in phones_data:
            IndividualPhone.objects.create(individual=individual, **phone)

        for email in emails_data:
            IndividualEmail.objects.create(individual=individual, **email)

    class Meta:
        model = Individual


class InboundContactAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactAddress


class InboundContactPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactPhone


class InboundContactEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InboundContactEmail


class InboundContactSerializer(serializers.ModelSerializer):
    address = InboundContactAddressSerializer()
    phones = InboundContactPhoneSerializer(many=True)
    emails = InboundContactEmailSerializer(many=True)

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

    class Meta:
        model = InboundContact


class OutboundContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutboundContact


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign


class SourceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SourceType


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
