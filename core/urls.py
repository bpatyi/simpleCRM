"""simpleCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import views

from django.conf.urls import (
    handler400,
    handler403,
    handler404,
    handler500
)

from core.views import (
    index,
    bad_request,
    permission_denied,
    page_not_found,
    server_error
)


handler400 = 'core.views.bad_request'
handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', index, name='index'),

    # own apps
    url(r'^accounts/', include('accounts.urls')),
    url(r'^crm/', include('crm.urls')),
    url(r'^api/', include('api.urls')),

    # installed app urls
    url(r'^select2/', include('django_select2.urls')),
]

if settings.DEBUG:
    from django.views.generic import TemplateView

    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^400/$', bad_request),
        url(r'^403/$', permission_denied),
        url(r'^404/$', page_not_found),
        url(r'^500/$', server_error),
    ]
