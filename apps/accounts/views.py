from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm
