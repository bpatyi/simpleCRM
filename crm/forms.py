import phonenumbers

from django.forms import (
    formset_factory,
    ModelForm,
    HiddenInput,
    ValidationError
)

from django.utils.translation import get_language

from crm.models import (
    Individual,
    IndividualAddress,
    IndividualEmail,
    IndividualPhone
)


class IndividualForm(ModelForm):

    class Meta:
        model = Individual
        exclude = ['id']


class IndividualAddressForm(ModelForm):

    class Meta:
        model = IndividualAddress
        exclude = ['id', 'individual']


class IndividualEmailForm(ModelForm):

    class Meta:
        model = IndividualEmail
        exclude = ['id', 'individual']


class IndividualPhoneForm(ModelForm):

    class Meta:
        model = IndividualPhone
        exclude = ['id', 'individual']
        widgets = {
            'type': HiddenInput()
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')

        try:
            number = phonenumbers.parse(number, self.data.get('country'))
        except phonenumbers.NumberParseException:
            raise ValidationError('We can not parse the given phone number.')

        if not phonenumbers.is_valid_number(number):
            raise ValidationError('The given phone number is not valid.')

        self.cleaned_data['type'] = IndividualPhone.get_type(
            phonenumbers.number_type(number)
        )

        return phonenumbers.format_number(
            number,
            phonenumbers.PhoneNumberFormat.E164
        )


IndividualEmailFormSet = formset_factory(IndividualEmailForm)
IndividualPhoneFormSet = formset_factory(IndividualPhoneForm)
