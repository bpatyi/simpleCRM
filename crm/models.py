import datetime

from django.db import models

from crm.abstracts import (
    AbstractBaseModel,
    AbstractCompanyModel,
    AbstractIndividualModel,
    AbstractAddressModel,
    AbstractEmailModel,
    AbstractPhoneModel,
)
from crm.enums import ContactType
from django.contrib.postgres.fields import ArrayField


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
    individual = models.ForeignKey("crm.Individual", related_name="address")

    class Meta:
        verbose_name_plural = "Individual addresses"


class IndividualEmail(AbstractEmailModel):
    individual = models.ForeignKey("crm.Individual", related_name="emails")


class IndividualPhone(AbstractPhoneModel):
    individual = models.ForeignKey("crm.Individual", related_name="phones")


class InboundContact(AbstractIndividualModel):
    individual = models.ForeignKey("crm.Individual", null=True, blank=True)
    source = models.ForeignKey("crm.Source", null=True)

    searchable_channels = ArrayField(
        models.CharField(
            max_length=1,
            choices=ContactType.get_choices()
        ),
        blank=True,
        null=True
    )

    @property
    def is_searchable(self):
        return self.searchable_channels is not None


class InboundContactAddress(AbstractAddressModel):
    inbound_contact = models.ForeignKey("crm.InboundContact", related_name="address")


class InboundContactEmail(AbstractEmailModel):
    inbound_contact = models.ForeignKey("crm.InboundContact", related_name="emails")


class InboundContactPhone(AbstractPhoneModel):
    inbound_contact = models.ForeignKey("crm.InboundContact", related_name="phones")


class OutboundContact(AbstractBaseModel):
    individual = models.ForeignKey("crm.Individual")
    campaign = models.ForeignKey("crm.Campaign", null=True)

    contact_type = models.CharField(
        max_length=1,
        choices=ContactType.get_choices(),
        null=True
    )
    date_of_contact = models.DateField(default=datetime.date.today)
    is_success = models.BooleanField(default=False)


class OutboundContactMailInfo(AbstractBaseModel):
    outbound_contact = models.ForeignKey("crm.OutboundContact", related_name="mail_info")
    address = models.ForeignKey("crm.IndividualAddress")

    is_deliverable = models.BooleanField(default=False)


class OutboundContactEmailInfo(AbstractBaseModel):
    outbound_contact = models.ForeignKey("crm.OutboundContact", related_name="email_infos")
    email = models.ForeignKey("crm.IndividualEmail")

    is_unsubscribed = models.BooleanField(default=False)
    is_soft_bounced = models.BooleanField(default=False)
    is_hard_bounced = models.BooleanField(default=False)

    open_times = ArrayField(models.DateTimeField(), blank=True)
    clicked_links = ArrayField(models.URLField(max_length=255), blank=True)

    @property
    def is_opened(self):
        return self.open_times is not None

    @property
    def is_clicked(self):
        return self.clicked_links is not None


class OutboundContactPhoneInfo(AbstractBaseModel):
    outbound_contact = models.ForeignKey("crm.OutboundContact", related_name="phone_infos")
    phone = models.ForeignKey("crm.IndividualPhone")

    is_available = models.BooleanField(default=False)

    call_times = ArrayField(models.DateTimeField(), blank=True)
    success_call_times = ArrayField(models.DateTimeField(), blank=True)


class Campaign(AbstractBaseModel):
    name = models.CharField(max_length=127)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


class SourceType(AbstractBaseModel):
    name = models.CharField(max_length=127)


class Source(AbstractBaseModel):
    name = models.CharField(max_length=127)
    type_of_source = models.ForeignKey("crm.SourceType", blank=True, null=True)
