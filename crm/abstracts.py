import phonenumbers

from django.db import models

from base.abstracts import AbstractBaseModel
from crm.enums import (
    Gender,
    FamilyStatus,
    EducationLevel,
    EntityType
)

from django_countries.fields import CountryField


class AbstractCompanyModel(AbstractBaseModel):
    name = models.CharField(verbose_name='Title', max_length=255)
    entity_type = models.CharField(
        verbose_name='Entity type',
        max_length=32,
        choices=EntityType.get_choices()
    )

    class Meta:
        abstract = True


class AbstractEmailModel(AbstractBaseModel):
    email = models.EmailField()

    class Meta:
        abstract = True


class AbstractPhoneModel(AbstractBaseModel):
    number = models.CharField(max_length=64)
    type = models.CharField(max_length=16, blank=True)

    class Meta:
        abstract = True

    @staticmethod
    def get_type(prototype):
        return {
            phonenumbers.PhoneNumberType.MOBILE: 'mobile',
            phonenumbers.PhoneNumberType.FIXED_LINE: 'line',
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: 'line or mobil',
            phonenumbers.PhoneNumberType.PAGER: 'pager',
            phonenumbers.PhoneNumberType.PERSONAL_NUMBER: 'personal number',
            phonenumbers.PhoneNumberType.PREMIUM_RATE: 'premium rate',
            phonenumbers.PhoneNumberType.SHARED_COST: 'shared cost',
            phonenumbers.PhoneNumberType.TOLL_FREE: 'toll free',
            phonenumbers.PhoneNumberType.UAN: 'uan',
            phonenumbers.PhoneNumberType.UNKNOWN: 'unknown',
        }.get(prototype, 'unknown')


class AbstractAddressModel(AbstractBaseModel):
    country = CountryField()
    zip_code = models.CharField(max_length=16)
    city = models.CharField(max_length=127)
    district = models.CharField(max_length=127)
    address = models.CharField(max_length=255)


class AbstractIndividualModel(AbstractBaseModel):
    gender = models.CharField(
        max_length=1,
        choices=Gender.get_choices()
    )
    title = models.CharField(max_length=127, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    family_status = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        choices=FamilyStatus.get_choices()
    )
    education_level = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        choices=EducationLevel.get_choices()
    )
    birth_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
