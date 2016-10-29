from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from crm.views import (
    Dashboard,
    IndividualList,
    IndividualDetail,
    IndividualCreate,
    IndividualEdit,
    IndividualDelete,
    IndividualAddOtherInfo,
    IndividualAddressCreate,
    IndividualAddressEdit,
    IndividualAddressDelete,
    IndividualEmailCreate,
    IndividualEmailEdit,
    IndividualEmailDelete,
    IndividualPhoneCreate,
    IndividualPhoneEdit,
    IndividualPhoneDelete
)

urlpatterns = [
    url('^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),

    # Individuals
    url(r'^individuals/$', IndividualList.as_view(), name='individual-list'),
    url(r'^individuals/(?P<pk>\d+)/$', IndividualDetail.as_view(), name='individual-detail'),
    url(r'^individuals/create/$', IndividualCreate.as_view(), name='individual-create'),
    url(r'^individuals/edit/(?P<pk>\d+)/$', IndividualEdit.as_view(), name='individual-edit'),
    url(r'^individuals/delete/(?P<pk>\d+)/$', IndividualDelete.as_view(), name='individual-edit'),
    url(r'^individuals/add-other-info/(?P<id>\d+)/$', IndividualAddOtherInfo.as_view(), name='individual-add-other-info'),

    # Individual address
    url(r'^individuals/(?P<pk>\d+)/create/address/$', IndividualAddressCreate.as_view(), name='individual-create-address'),
    url(r'^individuals/address/edit(?P<pk>\d+)/$', IndividualAddressEdit.as_view(), name='individual-edit-address'),
    url(r'^individuals/address/delete/(?P<pk>\d+)/$', IndividualAddressDelete.as_view(), name='individual-delete-address'),

    # Individual email
    url(r'^individuals/(?P<pk>\d+)/create/email/$', IndividualEmailCreate.as_view(),
        name='individual-create-email'),
    url(r'^individuals/email/edit(?P<pk>\d+)/$', IndividualEmailEdit.as_view(), name='individual-edit-email'),
    url(r'^individuals/email/delete/(?P<pk>\d+)/$', IndividualEmailDelete.as_view(),
        name='individual-delete-email'),

    # Individual phone
    url(r'^individuals/(?P<pk>\d+)/create/phone/$', IndividualPhoneCreate.as_view(),
        name='individual-create-phone'),
    url(r'^individuals/phone/edit(?P<pk>\d+)/$', IndividualPhoneEdit.as_view(), name='individual-edit-phone'),
    url(r'^individuals/phone/delete/(?P<pk>\d+)/$', IndividualPhoneDelete.as_view(),
        name='individual-delete-phone'),
]
