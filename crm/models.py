from django.db import models

from .abstracts import (
    AbstractBaseModel,
    AbstractCompanyModel,
    AbstractIndividualModel,
    AbstractNameModel,
    AbstractAddressModel,
    AbstractEmailModel,
    AbstractPhoneModel
)


class UserCompany(AbstractCompanyModel):
    created_by = models.ForeignKey("accounts.CustomUser")

    def get_by_name(self, name):
        return self.objects.get(name=name)


class UserCompanyManager(AbstractBaseModel):
    user_company_id = models.ForeignKey(UserCompany)
    user_id = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)


class Individual(AbstractIndividualModel):
    pass


class IndividualName(AbstractNameModel):
    individual_id = models.ForeignKey(Individual)


class IndividualAddress(AbstractAddressModel):
    individual_id = models.ForeignKey(Individual)


class IndividualEmail(AbstractEmailModel):
    individual_id = models.ForeignKey(Individual)


class IndividualPhone(AbstractPhoneModel):
    individual_id = models.ForeignKey(Individual)
