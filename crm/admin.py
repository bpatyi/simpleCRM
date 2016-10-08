from django.contrib import admin

from crm.models import (
    UserCompany
)


class UserCompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserCompany, UserCompanyAdmin)
