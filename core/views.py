from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views import View


class Index(View):
    template_name = 'index.html'

    def get(self, request):

        return render(
            request,
            self.template_name,
            {}
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
