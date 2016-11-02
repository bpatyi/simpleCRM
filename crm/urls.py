from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from crm.views import (
    CampaignCreate,
    CampaignDelete,
    CampaignEdit,
    CampaignList,
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
    IndividualPhoneDelete,
    SourceCreate,
    SourceDelete,
    SourceEdit,
    SourceList,
    SourceTypeCreate,
    SourceTypeDelete,
    SourceTypeEdit,
    SourceTypeList,
    InboundContactList,
    InboundContactDetail,
    OutboundContactList,
    OutboundContactDetail
)

urlpatterns = [
    url(
        r'^dashboard/$',
        login_required(Dashboard.as_view()),
        name='dashboard'
    ),

    # Campaign
    url(
        r'^campaigns/$',
        login_required(CampaignList.as_view()),
        name='campaign-list'
    ),
    url(
        r'^campaigns/create/$',
        login_required(CampaignCreate.as_view()),
        name='campaign-create'
    ),
    url(
        r'^campaigns/edit/(?P<pk>\d+)/$',
        login_required(CampaignEdit.as_view()),
        name='campaign-edit'
    ),
    url(
        r'^campaigns/delete/(?P<pk>\d+)/$',
        login_required(CampaignDelete.as_view()),
        name='campaign-delete'
    ),

    # Individuals
    url(
        r'^individuals/$',
        login_required(IndividualList.as_view()),
        name='individual-list'
    ),
    url(
        r'^individuals/(?P<pk>\d+)/$',
        login_required(IndividualDetail.as_view()),
        name='individual-detail'
    ),
    url(
        r'^individuals/create/$',
        login_required(IndividualCreate.as_view()),
        name='individual-create'
    ),
    url(
        r'^individuals/edit/(?P<pk>\d+)/$',
        login_required(IndividualEdit.as_view()),
        name='individual-edit'
    ),
    url(
        r'^individuals/delete/(?P<pk>\d+)/$',
        login_required(IndividualDelete.as_view()),
        name='individual-delete'
    ),
    url(
        r'^individuals/add-other-info/(?P<id>\d+)/$',
        login_required(IndividualAddOtherInfo.as_view()),
        name='individual-add-other-info'
    ),

    # Individual address
    url(
        r'^individuals/(?P<pk>\d+)/create/address/$',
        login_required(IndividualAddressCreate.as_view()),
        name='individual-create-address'
    ),
    url(
        r'^individuals/address/edit(?P<pk>\d+)/$',
        login_required(IndividualAddressEdit.as_view()),
        name='individual-edit-address'
    ),
    url(
        r'^individuals/address/delete/(?P<pk>\d+)/$',
        login_required(IndividualAddressDelete.as_view()),
        name='individual-delete-address'
    ),

    # Individual email
    url(
        r'^individuals/(?P<pk>\d+)/create/email/$',
        login_required(IndividualEmailCreate.as_view()),
        name='individual-create-email'
    ),
    url(
        r'^individuals/email/edit(?P<pk>\d+)/$',
        login_required(IndividualEmailEdit.as_view()),
        name='individual-edit-email'
    ),
    url(
        r'^individuals/email/delete/(?P<pk>\d+)/$',
        login_required(IndividualEmailDelete.as_view()),
        name='individual-delete-email'
    ),

    # Individual phone
    url(
        r'^individuals/(?P<pk>\d+)/create/phone/$',
        login_required(IndividualPhoneCreate.as_view()),
        name='individual-create-phone'
    ),
    url(
        r'^individuals/phone/edit(?P<pk>\d+)/$',
        login_required(IndividualPhoneEdit.as_view()),
        name='individual-edit-phone'
    ),
    url(
        r'^individuals/phone/delete/(?P<pk>\d+)/$',
        login_required(IndividualPhoneDelete.as_view()),
        name='individual-delete-phone'
    ),

    # Source type
    url(
        r'^source-types/$',
        login_required(SourceTypeList.as_view()),
        name='source-type-list'
    ),
    url(
        r'^source-types/create/$',
        login_required(SourceTypeCreate.as_view()),
        name='source-type-create'
    ),
    url(
        r'^source-types/edit/(?P<pk>\d+)/$',
        login_required(SourceTypeEdit.as_view()),
        name='source-type-edit'
    ),
    url(
        r'^source-types/delete/(?P<pk>\d+)/$',
        login_required(SourceTypeDelete.as_view()),
        name='source-type-delete'
    ),

    # Source
    url(
        r'^sources/$',
        login_required(SourceList.as_view()),
        name='source-list'
    ),
    url(
        r'^sources/create/$',
        login_required(SourceCreate.as_view()),
        name='source-create'
    ),
    url(
        r'^sources/edit/(?P<pk>\d+)/$',
        login_required(SourceEdit.as_view()),
        name='campaign-edit'
    ),
    url(
        r'^sources/delete/(?P<pk>\d+)/$',
        login_required(SourceDelete.as_view()),
        name='source-delete'
    ),

    url(
        r'^inbound-contacts/$',
        login_required(InboundContactList.as_view()),
        name='inbound-contact-list'
    ),
    url(
        r'^inbound-contacts/(?P<pk>\d+)/$',
        login_required(InboundContactDetail.as_view()),
        name='inbound-contact-detail'
    ),
    url(
        r'^outbound-contacts/$',
        login_required(OutboundContactList.as_view()),
        name='outbound-contact-list'
    ),
    url(
        r'^outbound-contacts/(?P<pk>\d+)/$',
        login_required(OutboundContactDetail.as_view()),
        name='outbound-contact-detail'
    ),
]
