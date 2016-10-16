from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect

from crm.forms import (
    IndividualForm,
    IndividualAddressForm,
    IndividualPhoneFormSet,
    IndividualEmailFormSet
)
from crm.models import (
    Individual,
    IndividualAddress,
    IndividualPhone,
    IndividualEmail
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


class IndividualCreate(View):
    template_name = 'individual_form.html'

    def get(self, request):

        context = {
            'form': IndividualForm(),
            'address_form': IndividualAddressForm(),
            'form_sets': {
                'email': {
                    'title': 'Emails',
                    'form_set': IndividualEmailFormSet(prefix="email"),
                },
                'phone': {
                    'title': 'Phones',
                    'form_set': IndividualPhoneFormSet(prefix="phone")
                }
            }
        }

        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = IndividualForm(request.POST)
        address_form = IndividualAddressForm(request.POST)
        email_form_set = IndividualEmailFormSet(
            request.POST,
            request.FILES,
            prefix="email"
        )
        phone_form_set = IndividualPhoneFormSet(
            request.POST,
            request.FILES,
            prefix="phone"
        )

        if not form.is_valid() or \
           not address_form.is_valid() or \
           not email_form_set.is_valid() or \
           not phone_form_set.is_valid():

            context = {
                'form': form,
                'address_form': address_form,
                'form_sets': {
                    'email': {
                        'title': 'Emails',
                        'form_set': email_form_set,
                    },
                    'phone': {
                        'title': 'Phones',
                        'form_set': phone_form_set
                    }
                }
            }

            return render(
                request,
                self.template_name,
                context
            )

        individual = form.save(commit=True)

        address = IndividualAddress.objects.create(
            individual_id=individual.id,
            country=address_form.cleaned_data.get('country'),
            zip_code=address_form.cleaned_data.get('zip_code'),
            city=address_form.cleaned_data.get('city'),
            district=address_form.cleaned_data.get('district'),
            address=address_form.cleaned_data.get('address')
        )

        for form in email_form_set:
            email = IndividualEmail.objects.create(
                individual_id=individual.id,
                email=form.cleaned_data.get('email')
            )

        for form in phone_form_set:
            phone = IndividualPhone.objects.create(
                individual_id=individual.id,
                number=form.cleaned_data.get('number'),
                type=form.cleaned_data.get('type')
            )

        return redirect('individual-list')
