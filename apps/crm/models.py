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
from apps.accounts.models import CustomUser


class UserCompany(AbstractCompanyModel):
    created_by = models.ForeignKey(CustomUser)


class UserCompanyManager(AbstractBaseModel):
    user_company_id = models.ForeignKey(UserCompany)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


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

