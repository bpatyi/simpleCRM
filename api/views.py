from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework import generics, permissions, parsers

from rest_framework_docs.api_docs import ApiDocumentation
from rest_framework_docs.settings import DRFSettings

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


class ApiEndpoints(TemplateView):
    template_name = "endpoints.html"

    def get_context_data(self, **kwargs):
        settings = DRFSettings().settings
        if settings["HIDE_DOCS"]:
            raise Http404("Django Rest Framework Docs are hidden. Check your settings.")

        context = super(ApiEndpoints, self).get_context_data(**kwargs)
        docs = ApiDocumentation()
        endpoints = docs.get_endpoints()

        query = self.request.GET.get("search", "")
        if query and endpoints:
            endpoints = [endpoint for endpoint in endpoints if query in endpoint.path]

        for endpoint in endpoints:
            if '<pk>' in endpoint.path:
                endpoint.link = endpoint.path.replace('<pk>', '0')
            else:
                endpoint.link = endpoint.path

        context['query'] = query
        context['endpoints'] = endpoints
        return context


class IndividualListAPI(generics.ListAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IndividualCreateAPI(generics.CreateAPIView):
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (parsers.MultiPartParser, parsers.FormParser,)


class IndividualRetrieveAPI(generics.RetrieveAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IndividualUpdateAPI(generics.UpdateAPIView):
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class IndividualDestroyAPI(generics.DestroyAPIView):
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InboundContactListAPI(generics.ListAPIView):
    queryset = InboundContact.objects.all()
    serializer_class = InboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InboundContactCreateAPI(generics.CreateAPIView):
    serializer_class = InboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InboundContactRetrieveAPI(generics.RetrieveAPIView):
    queryset = InboundContact.objects.all()
    serializer_class = InboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InboundContactUpdateAPI(generics.UpdateAPIView):
    serializer_class = InboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InboundContactDestroyAPI(generics.DestroyAPIView):
    serializer_class = InboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OutboundContactListAPI(generics.ListAPIView):
    queryset = OutboundContact.objects.all()
    serializer_class = OutboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OutboundContactCreateAPI(generics.CreateAPIView):
    serializer_class = OutboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OutboundContactRetrieveAPI(generics.RetrieveAPIView):
    queryset = OutboundContact.objects.all()
    serializer_class = OutboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OutboundContactUpdateAPI(generics.UpdateAPIView):
    serializer_class = OutboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OutboundContactDestroyAPI(generics.DestroyAPIView):
    serializer_class = OutboundContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignListAPI(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignCreateAPI(generics.CreateAPIView):
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignRetrieveAPI(generics.RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignUpdateAPI(generics.UpdateAPIView):
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CampaignDestroyAPI(generics.DestroyAPIView):
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceTypeListAPI(generics.ListAPIView):
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceTypeCreateAPI(generics.CreateAPIView):
    serializer_class = SourceTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceTypeRetrieveAPI(generics.RetrieveAPIView):
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceTypeUpdateAPI(generics.UpdateAPIView):
    serializer_class = SourceTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceTypeDestroyAPI(generics.DestroyAPIView):
    serializer_class = SourceTypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceListAPI(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceCreateAPI(generics.CreateAPIView):
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceRetrieveAPI(generics.RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceUpdateAPI(generics.UpdateAPIView):
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SourceDestroyAPI(generics.DestroyAPIView):
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
