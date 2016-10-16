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
    individual = models.ForeignKey("crm.Individual")


class InboundContactAddress(AbstractAddressModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")


class InboundContactEmail(AbstractEmailModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")


class InboundContactPhone(AbstractPhoneModel):
    inbound_contact = models.ForeignKey("crm.InboundContact")

class OutboundContact(models.Model):
    individual = models.ForeignKey("crm.Individual")
