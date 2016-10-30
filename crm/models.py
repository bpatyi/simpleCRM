from django.db import models

from crm.abstracts import (
    AbstractBaseModel,
    AbstractCompanyModel,
    AbstractIndividualModel,
    AbstractAddressModel,
    AbstractEmailModel,
    AbstractPhoneModel
)


class UserCompany(AbstractCompanyModel):
    created_by = models.ForeignKey("accounts.CustomUser")

    class Meta:
        verbose_name_plural = "User companies"

    def __str__(self):
        return self.name

    def get_by_name(self, name):
        return self.objects.get(name=name)


class UserCompanyConnection(AbstractBaseModel):
    company = models.ForeignKey("crm.UserCompany")
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return ' - '.join([self.user.username, self.company.name])


class Individual(AbstractIndividualModel):
    pass

    def __str__(self):
        return ' '.join([self.title, self.first_name, self.last_name])


class IndividualAddress(AbstractAddressModel):
    individual = models.ForeignKey("crm.Individual")

    class Meta:
        verbose_name_plural = "Individual addresses"


class IndividualEmail(AbstractEmailModel):
    individual = models.ForeignKey("crm.Individual")


class IndividualPhone(AbstractPhoneModel):
    individual = models.ForeignKey("crm.Individual")


class InboundContact(AbstractIndividualModel):
    individual = models.ForeignKey("crm.Individual", null=True, blank=True)
    source = models.ForeignKey("crm.Source")


class InboundContactAddress(AbstractAddressModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")


class InboundContactEmail(AbstractEmailModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")


class InboundContactPhone(AbstractPhoneModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")


class OutboundContact(models.Model):
    individual = models.ForeignKey("crm.Individual")


class Campaign(AbstractBaseModel):
    name = models.CharField(max_length=127)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class SourceType(AbstractBaseModel):
    name = models.CharField(max_length=127)


class Source(AbstractBaseModel):
    name = models.CharField(max_length=127)
    type_of_source = models.ForeignKey("crm.SourceType", blank=True, null=True)
