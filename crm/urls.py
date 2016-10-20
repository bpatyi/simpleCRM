from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from crm.views import (
    Dashboard,
    IndividualList,
    IndividualDetail,
    IndividualCreate,
    IndividualEdit
)

urlpatterns = [
    url('^dashboard/$', login_required(Dashboard.as_view()), name='dashboard'),

    # Individuals
    url(r'^individuals/$', IndividualList.as_view(), name='individual-list'),
    url(r'^individuals/(?P<pk>\d+)/$', IndividualDetail.as_view(), name='individual-detail'),
    url(r'^individuals/create/$', IndividualCreate.as_view(), name='individual-create'),
    url(r'^individuals/edit/(?P<id>\d+)/$', IndividualEdit.as_view(), name='individual-edit'),
]
