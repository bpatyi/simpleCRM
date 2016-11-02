from django.shortcuts import render

from rest_framework import generics

from api.serializers import (
    IndividualSerializer,
    InboundContactSerializer,
    OutboundContactSerializer,
    CampaignSerializer,
    SourceSerializer,
    SourceTypeSerializer
)

from crm.models import (
    Individual,
    InboundContact,
    OutboundContact,
    Source,
    Campaign,
    SourceType
)


class IndividualListAPI(generics.ListAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class IndividualCreateAPI(generics.CreateAPIView):
    serializer_class = IndividualSerializer


class IndividualRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = IndividualSerializer


class IndividualUpdateAPI(generics.UpdateAPIView):
    serializer_class = IndividualSerializer


class IndividualDestroyAPI(generics.DestroyAPIView):
    serializer_class = IndividualSerializer


class InboundContactListAPI(generics.ListAPIView):
    queryset = InboundContact.objects.all()
    serializer_class = InboundContactSerializer


class InboundContactCreateAPI(generics.CreateAPIView):
    serializer_class = InboundContactSerializer


class InboundContactRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = InboundContactSerializer


class InboundContactUpdateAPI(generics.UpdateAPIView):
    serializer_class = InboundContactSerializer


class InboundContactDestroyAPI(generics.DestroyAPIView):
    serializer_class = InboundContactSerializer


class OutboundContactListAPI(generics.ListAPIView):
    queryset = OutboundContact.objects.all()
    serializer_class = OutboundContactSerializer


class OutboundContactCreateAPI(generics.CreateAPIView):
    serializer_class = OutboundContactSerializer


class OutboundContactRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = OutboundContactSerializer


class OutboundContactUpdateAPI(generics.UpdateAPIView):
    serializer_class = OutboundContactSerializer


class OutboundContactDestroyAPI(generics.DestroyAPIView):
    serializer_class = OutboundContactSerializer


class CampaignListAPI(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignCreateAPI(generics.CreateAPIView):
    serializer_class = CampaignSerializer


class CampaignRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = CampaignSerializer


class CampaignUpdateAPI(generics.UpdateAPIView):
    serializer_class = CampaignSerializer


class CampaignDestroyAPI(generics.DestroyAPIView):
    serializer_class = CampaignSerializer


class SourceTypeListAPI(generics.ListAPIView):
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer


class SourceTypeCreateAPI(generics.CreateAPIView):
    serializer_class = SourceTypeSerializer


class SourceTypeRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = SourceTypeSerializer


class SourceTypeUpdateAPI(generics.UpdateAPIView):
    serializer_class = SourceTypeSerializer


class SourceTypeDestroyAPI(generics.DestroyAPIView):
    serializer_class = SourceTypeSerializer


class SourceListAPI(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceCreateAPI(generics.CreateAPIView):
    serializer_class = SourceSerializer


class SourceRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = SourceSerializer


class SourceUpdateAPI(generics.UpdateAPIView):
    serializer_class = SourceSerializer


class SourceDestroyAPI(generics.DestroyAPIView):
    serializer_class = SourceSerializer
