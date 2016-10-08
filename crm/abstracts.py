from django.db import models

from base.abstracts import AbstractBaseModel


class AbstractCompanyModel(AbstractBaseModel):
    name = models.CharField(verbose_name='Title', max_length=255)
    entity_type = models.CharField(verbose_name='Entity type', max_length=32)

    class Meta:
        abstract = True


class AbstractEmailModel(AbstractBaseModel):
    email = models.EmailField()

    class Meta:
        abstract = True


class AbstractPhoneModel(AbstractBaseModel):
    number = models.CharField(max_length=64)
    type = models.CharField(max_length=16)

    class Meta:
        abstract = True


class AbstractAddressModel(AbstractBaseModel):
    country_code = models.CharField(max_length=8)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=16)
    city = models.CharField(max_length=127)
    district = models.CharField(max_length=127)
    address = models.CharField(max_length=255)


class AbstractNameModel(AbstractBaseModel):
    title = models.CharField(max_length=127, blank=True, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class AbstractIndividualModel(AbstractBaseModel):
    gender = models.CharField(max_length=1)
    family_status = models.CharField(max_length=32)
    education_level = models.CharField(max_length=32)

    class Meta:
        abstract = True
