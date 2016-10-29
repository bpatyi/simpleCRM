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
    IndividualEmailForm
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


# class IndividualCreate(View):
#     template_name = 'individual_form.html'
#
#     def get(self, request):
#
#         context = {
#             'form': IndividualForm(),
#             'address_form': IndividualAddressForm(prefix='address', instance=Individual()),
#             'form_sets': {
#                 'email': {
#                     'title': 'Emails',
#                     'form_set': IndividualEmailFormSet(prefix="email", instance=Individual()),
#                 },
#                 'phone': {
#                     'title': 'Phones',
#                     'form_set': IndividualPhoneFormSet(prefix="phone", instance=Individual())
#                 }
#             }
#         }
#
#         return render(
#             request,
#             self.template_name,
#             context
#         )
#
#     def post(self, request):
#         form = IndividualForm(request.POST)
#
#         if not form.is_valid():
#             context = {
#                 'form': form,
#                 'address_form': IndividualAddressForm(request.POST, prefix="address"),
#                 'form_sets': {
#                     'email': {
#                         'title': 'Emails',
#                         'form_set': IndividualEmailFormSet(request.POST, prefix="email"),
#                     },
#                     'phone': {
#                         'title': 'Phones',
#                         'form_set': IndividualPhoneFormSet(request.POST, prefix="phone")
#                     }
#                 }
#             }
#
#         individual = form.save(commit=False)
#
#         address_form = IndividualAddressForm(request.POST, prefix="address", instance=individual)
#         email_form_set = IndividualEmailFormSet(request.POST, prefix="email", instance=individual)
#         phone_form_set = IndividualPhoneFormSet(request.POST, prefix="phone", instance=individual)
#
#         if not address_form.is_valid() or \
#            not email_form_set.is_valid() or \
#            not phone_form_set.is_valid():
#
#             context = {
#                 'form': form,
#                 'address_form': address_form,
#                 'form_sets': {
#                     'email': {
#                         'title': 'Emails',
#                         'form_set': email_form_set,
#                     },
#                     'phone': {
#                         'title': 'Phones',
#                         'form_set': phone_form_set
#                     }
#                 }
#             }
#
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
#
#         individual = form.save(commit=True)
#         address_form = IndividualAddressForm(request.POST, prefix="address", instance=individual)
#         address_form.save()
#
#         email_form_set = IndividualEmailFormSet(request.POST, prefix="email", instance=individual)
#
#         if not email_form_set.is_valid():
#             raise Exception("mi fasz van")
#
#         email_form_set.save()
#
#         phone_form_set = IndividualPhoneFormSet(request.POST, prefix="phone", instance=individual)
#
#         if not phone_form_set.is_valid():
#             raise Exception("mi fasz 32")
#
#         phone_form_set.save()
#         # address = IndividualAddress.objects.create(
#         #     individual_id=individual.id,
#         #     country=address_form.cleaned_data.get('country'),
#         #     zip_code=address_form.cleaned_data.get('zip_code'),
#         #     city=address_form.cleaned_data.get('city'),
#         #     district=address_form.cleaned_data.get('district'),
#         #     address=address_form.cleaned_data.get('address')
#         # )
#
#         # for form in email_form_set:
#         #     if form.cleaned_data:
#         #         email = IndividualEmail.objects.create(
#         #             individual_id=individual.id,
#         #             email=form.cleaned_data.get('email')
#         #         )
#
#         # for form in phone_form_set:
#         #     if form.cleaned_data:
#         #         phone = IndividualPhone.objects.create(
#         #             individual_id=individual.id,
#         #             number=form.cleaned_data.get('number'),
#         #             type=form.cleaned_data.get('type')
#         #         )
#
#         return redirect('individual-list')
#
#
# class IndividualEdit(View):
#     template_name = "individual_form.html"
#
#     def get(self, request, id):
#         individual = get_object_or_404(Individual, id=id)
#         emails = individual.individualemail_set.all()
#         phones = individual.individualphone_set.all()
#
#         context = {
#             'form': IndividualForm(instance=individual),
#             'address_form': IndividualAddressForm(
#                 instance=IndividualAddress.objects.filter(individual_id=id)
#             ),
#             'form_sets': {
#                 'email': {
#                     'title': 'Emails',
#                     'form_set': IndividualEmailFormSet(
#                         prefix="email",
#                         initial=[email.__dict__ for email in emails] if emails else None
#                     ),
#                 },
#                 'phone': {
#                     'title': 'Phones',
#                     'form_set': IndividualPhoneFormSet(
#                         prefix="phone",
#                         initial=[phone.__dict__ for phone in phones] if phones else None
#                     )
#                 }
#             }
#         }
#
#         return render(
#             request,
#             self.template_name,
#             context
#         )
#
#     def post(self, request, id):
#         individual = get_object_or_404(Individual, id=id)
#         emails = individual.individualemail_set.all()
#         phones = individual.individualphone_set.all()
#
#
#         form = IndividualForm(
#             request.POST,
#             instance=individual
#         )
#         address_form = IndividualAddressForm(
#             request.POST,
#             instance=IndividualAddress.objects.get(individual_id=individual.id)
#         )
#         email_form_set = IndividualEmailFormSet(
#             request.POST,
#             prefix="email",
#             initial=[email.__dict__ for email in emails] if emails else None
#         )
#         phone_form_set = IndividualPhoneFormSet(
#             request.POST,
#             prefix="phone",
#             initial=[phone.__dict__ for phone in phones] if phones else None
#         )
#
#         if not form.is_valid() or \
#            not address_form.is_valid() or \
#            not email_form_set.is_valid() or \
#            not phone_form_set.is_valid():
#
#             context = {
#                 'form': form,
#                 'address_form': address_form,
#                 'form_sets': {
#                     'email': {
#                         'title': 'Emails',
#                         'form_set': email_form_set,
#                     },
#                     'phone': {
#                         'title': 'Phones',
#                         'form_set': phone_form_set
#                     }
#                 }
#             }
#
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
#
#         individual = form.save()
#         address = IndividualAddress.objects.update(
#             individual_id=individual.id,
#             country=address_form.cleaned_data.get('country'),
#             zip_code=address_form.cleaned_data.get('zip_code'),
#             city=address_form.cleaned_data.get('city'),
#             district=address_form.cleaned_data.get('district'),
#             address=address_form.cleaned_data.get('address')
#         )
#
#         print(email_form_set.deleted_forms)
#         #for form in email_form_set:
#         #    if form['id'].value() in marked_for_delete_ids:
#         #        IndividualEmail.objects.delete(form.get('id'))
#
#         #    email = IndividualEmail.objects.get(individual_id=individual.id)
#         #    if not email:
#         #        IndividualEmail.objects.create(
#         #            individual_id=individual.id,
#         #            email=form.cleaned_data.get('email')
#         #        )
#         #    elif email.email != form.cleaned_data.get('email'):
#         #        email.update(email=email)
#
#         print(phone_form_set.deleted_forms)
#         #for form in phone_form_set:
#         #    if form['id'].value() in marked_for_delete_ids:
#         #        IndividualPhone.objects.delete(form.get('id'))
#
#         #    phone = IndividualPhone.objects.get(individual_id=individual.id)
#         #    if not phone:
#         #        IndividualPhone.objects.create(
#         #            individual_id=individual.id,
#         #            number=form.cleaned_data.get('number'),
#         #            type=form.cleaned_data.get('type')
#         #        )
#         #    elif phone.number != form.cleaned_data.get('number') or phone.type != form.cleaned_data.get('type'):
#         #        phone.update(number=form.cleaned_data.get('number'), type=form.cleaned_data.get('type'))
#
#         return redirect('individual-list')