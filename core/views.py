from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):

    return render_to_response(
        'index.html'
    )


def bad_request(request):
    response = render_to_response(
        '400.html',
        RequestContext(request)
    )

    response.status_code = 400

    return response


def permission_denied(request):
    response = render_to_response(
        '403.html',
        RequestContext(request)
    )

    response.status_code = 403

    return response


def page_not_found(request):
    response = render_to_response(
        '404.html',
        RequestContext(request)
    )

    response.status_code = 404

    return response


def server_error(request):
    response = render_to_response(
        '500.html',
        RequestContext(request)
    )

    response.status_code = 500

    return response
