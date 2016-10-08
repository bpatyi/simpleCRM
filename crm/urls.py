from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import Dashboard

urlpatterns = [
    url('^dashboard/$', login_required(Dashboard.as_view()), name='dashboard')
]
