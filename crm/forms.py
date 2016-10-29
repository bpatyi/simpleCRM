import phonenumbers

from django.forms import (
    ModelForm,
    HiddenInput,
    ValidationError
)
from django.core.validators import validate_email

from base.utils import GeoCoder
from crm.models import (
    Individual,
    IndividualAddress,
    IndividualEmail,
    IndividualPhone
)


class IndividualForm(ModelForm):

    class Meta:
        model = Individual
        exclude = ['id', 'is_valid', 'is_cleansed']


class IndividualAddressForm(ModelForm):

    class Meta:
        model = IndividualAddress
        exclude = ['id']
        widgets = {
            'individual': HiddenInput(),
            'county': HiddenInput(),
            'postal_code_suffix': HiddenInput(),
            'administrative_area': HiddenInput(),
            'final_type': HiddenInput(),
            'formatted_address': HiddenInput(),
            'longitude': HiddenInput(),
            'latitude': HiddenInput(),
            'is_valid': HiddenInput(),
            'is_cleansed': HiddenInput()
        }

    def clean(self):
        data = self.cleaned_data

        address = ' '.join([
            data.get('locality'),
            data.get('route'),
            str(data.get('street_number')),
            data.get('postal_code'),
            data.get('country')
        ])

        geocode = GeoCoder.geocode(address)

        if geocode.is_valid_address():
            data['country'] = geocode.country
            data['postal_code'] = geocode.postal_code
            data['postal_code_suffix'] = geocode.postal_code_suffix
            data['county'] = geocode.county
            data['administrative_area'] = geocode.administrative_area
            data['locality'] = geocode.locality
            data['district'] = geocode.district
            data['route'] = geocode.route
            data['street_number'] = geocode.street_number
            data['final_type'] = geocode.type
            data['formatted_address'] = geocode.formatted_address
            data['latitude'] = geocode.latitude
            data['longitude'] = geocode.longitude

            data['is_valid'] = True
            data['is_cleansed'] = True

        return data


class IndividualEmailForm(ModelForm):

    class Meta:
        model = IndividualEmail
        exclude = ['id', 'is_cleansed']
        widgets = {
            'individual': HiddenInput(),
            'is_valid': HiddenInput()
        }

    def clean(self):
        self.cleaned_data['is_valid'] = True

        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        validate_email(email)

        return email


class IndividualPhoneForm(ModelForm):
    number = None

    class Meta:
        model = IndividualPhone
        exclude = ['id', 'is_cleansed']
        widgets = {
            'type': HiddenInput(),
            'individual': HiddenInput(),
            'is_valid': HiddenInput()
        }

    def clean(self):
        data = self.cleaned_data

        data["type"] = IndividualPhone.get_type(
            phonenumbers.number_type(self.number)
        )
        data['is_valid'] = True

        return data

    def clean_number(self):
        number = self.cleaned_data.get('number')

        try:
            self.number = phonenumbers.parse(number, self.cleaned_data.get('country'))
        except phonenumbers.NumberParseException:
            raise ValidationError('We can not parse the given phone number.')

        if not phonenumbers.is_valid_number(self.number):
            raise ValidationError('The given phone number is not valid.')

        return phonenumbers.format_number(
            self.number,
            phonenumbers.PhoneNumberFormat.E164
        )