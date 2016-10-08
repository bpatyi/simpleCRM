from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm


class Registration(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = CustomUserCreationForm()

        context = {
            "form": form
        }

        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

        context = {
            "form": form
        }

        return render(
            request,
            self.template_name,
            context
        )
