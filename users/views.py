from typing import Any
from django import http
from django.shortcuts import redirect, render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import UserAdminCreationForm
from django.conf import settings
from django.contrib import messages
# Create your views here.
from django.views.generic import TemplateView
from .forms import LoginForm


class SignUpView(FormView):
    form_class = UserAdminCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def dispatch(
        self, request: http.HttpRequest, *args: Any, **kwargs: Any
    ) -> http.HttpResponse:
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Account creation successful")
        return super(SignUpView, self).form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
