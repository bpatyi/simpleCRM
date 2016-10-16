from django.contrib import admin

from crm.models import (
    UserCompany,
    UserCompanyConnection,
    Individual,
    IndividualEmail,
    IndividualAddress,
    IndividualPhone
)


class UserCompanyAdmin(admin.ModelAdmin):
    exclude = ['id']


class UserCompanyConnectionAdmin(admin.ModelAdmin):
    exclude = ['id']


class IndividualAdmin(admin.ModelAdmin):
    exclude = ['id']


class IndividualAddressAdmin(admin.ModelAdmin):
    exclude = ['id']


class IndividualEmailAdmin(admin.ModelAdmin):
    exclude = ['id']


class IndividualPhoneAdmin(admin.ModelAdmin):
    exclude = ['id']

admin.site.register(UserCompany, UserCompanyAdmin)
admin.site.register(UserCompanyConnection, UserCompanyConnectionAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(IndividualAddress, IndividualAddressAdmin)
admin.site.register(IndividualEmail, IndividualEmailAdmin)
admin.site.register(IndividualPhone, IndividualPhoneAdmin)
