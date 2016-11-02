from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from crm.forms import (
    IndividualForm,
    IndividualAddressForm,
    IndividualPhoneForm,
    IndividualEmailForm,
    SourceTypeForm,
    SourceForm,
    CampaignForm
)
from crm.models import (
    Individual,
    IndividualAddress,
    IndividualPhone,
    IndividualEmail,
    SourceType,
    Source,
    Campaign,
    InboundContact,
    OutboundContact
)


class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):

        context = {}

        return render(
            request,
            self.template_name,
            context
        )


class IndividualList(ListView):
    model = Individual
    template_name = 'individual_list.html'


class IndividualDetail(DetailView):
    model = Individual
    template_name = 'individual_detail.html'


class IndividualCreate(CreateView):
    template_name = 'individual_form.html'
    model = Individual
    form_class = IndividualForm

    def get_success_url(self):
        return reverse('individual-add-other-info', args=[self.object.id])


class IndividualEdit(UpdateView):
    template_name = 'individual_form.html'
    model = Individual
    form_class = IndividualForm

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.id])


class IndividualDelete(DeleteView):
    model = Individual
    success_url = reverse_lazy('individual-list')
    template_name = 'confirm_delete.html'


class IndividualAddOtherInfo(View):
    template_name = "individual_other_form.html"

    def get(self, request, id):
        individual = get_object_or_404(Individual, id=id)

        context = {
            'forms': {
                'address': IndividualAddressForm(initial={'individual': individual}),
                'phone': IndividualPhoneForm(initial={'individual': individual}),
                'email': IndividualEmailForm(initial={'individual': individual})
            }
        }

        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, id):
        individual = get_object_or_404(Individual, id=id)

        address_form = IndividualAddressForm(request.POST)
        phone_form = IndividualPhoneForm(request.POST)
        email_form = IndividualEmailForm(request.POST)

        if not address_form.is_valid() or not phone_form.is_valid() or not email_form.is_valid():

            return render(
                request,
                self.template_name,
                {
                    'forms': {
                        'address': address_form,
                        'phone': phone_form,
                        'email': email_form
                    }
                },
            )

        address_form.save()
        phone_form.save()
        email_form.save()

        return redirect('individual-list')


class IndividualAddressCreate(CreateView):
    model = IndividualAddress
    template_name = 'create_form.html'
    form_class = IndividualAddressForm

    def get(self, request, *args, **kwargs):
        individual = get_object_or_404(Individual, pk=kwargs.get('pk'))
        form = self.form_class(initial={'individual': individual})

        context = {
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualAddressEdit(UpdateView):
    model = IndividualAddress
    template_name = 'create_form.html'
    form_class = IndividualAddressForm

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualAddressDelete(DeleteView):
    model = IndividualAddress
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualPhoneCreate(CreateView):
    model = IndividualPhone
    template_name = 'create_form.html'
    form_class = IndividualPhoneForm

    def get(self, request, *args, **kwargs):
        individual = get_object_or_404(Individual, pk=kwargs.get('pk'))
        form = self.form_class(initial={'individual': individual})

        context = {
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualPhoneEdit(UpdateView):
    model = IndividualPhone
    template_name = 'create_form.html'
    form_class = IndividualPhoneForm

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualPhoneDelete(DeleteView):
    model = IndividualPhone
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualEmailCreate(CreateView):
    model = IndividualEmail
    template_name = 'create_form.html'
    form_class = IndividualEmailForm

    def get(self, request, *args, **kwargs):
        individual = get_object_or_404(Individual, pk=kwargs.get('pk'))
        form = self.form_class(initial={'individual': individual})

        context = {
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualEmailEdit(UpdateView):
    model = IndividualEmail
    template_name = 'create_form.html'
    form_class = IndividualEmailForm

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class IndividualEmailDelete(DeleteView):
    model = IndividualEmail
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse('individual-detail', args=[self.object.individual.id])


class SourceTypeList(ListView):
    model = SourceType
    template_name = 'source_type_list.html'


class SourceTypeCreate(CreateView):
    template_name = 'source_type_form.html'
    model = SourceType
    form_class = SourceTypeForm

    def get_success_url(self):
        return reverse('source-type-list')


class SourceTypeEdit(UpdateView):
    template_name = 'source_type_form.html'
    model = SourceType
    form_class = SourceTypeForm

    def get_success_url(self):
        return reverse('source-type-list')


class SourceTypeDelete(DeleteView):
    model = SourceType
    success_url = reverse_lazy('source-type-list')
    template_name = 'confirm_delete.html'


class SourceList(ListView):
    model = Source
    template_name = 'source_list.html'


class SourceCreate(CreateView):
    template_name = 'source_form.html'
    model = Source
    form_class = SourceForm

    def get_success_url(self):
        return reverse('source-list')


class SourceEdit(UpdateView):
    template_name = 'source_form.html'
    model = Source
    form_class = SourceForm

    def get_success_url(self):
        return reverse('source-list')


class SourceDelete(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'confirm_delete.html'


class CampaignList(ListView):
    model = Campaign
    template_name = 'campaign_list.html'


class CampaignCreate(CreateView):
    template_name = 'campaign_form.html'
    model = Campaign
    form_class = CampaignForm

    def get_success_url(self):
        return reverse('campaign-list')


class CampaignEdit(UpdateView):
    template_name = 'campaign_form.html'
    model = Campaign
    form_class = CampaignForm

    def get_success_url(self):
        return reverse('Campaign-list')


class CampaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign-list')
    template_name = 'confirm_delete.html'


class InboundContactList(ListView):
    model = InboundContact
    template_name = 'inbound_contact_list.html'


class InboundContactDetail(DetailView):
    model = InboundContact
    template_name = 'inbound_contact_detail.html'


class OutboundContactList(ListView):
    model = OutboundContact
    template_name = 'outbound_contact_list.html'


class OutboundContactDetail(DetailView):
    model = OutboundContact
    template_name = 'outbound_contact_detail.html'
