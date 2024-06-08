from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


class LandinHomeView(TemplateView):
    template_name = "pages/home.html"


class LandinAboutView(TemplateView):
    template_name = "pages/about.html"


class LandinContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = "/contact-us/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.request.user.is_authenticated:
            instance.user = self.request.user
            instance.save()
        form.save()
        messages.success(self.request, "Contact saved successfully")
        return super().form_valid(form)


class LandinPricingView(TemplateView):
    template_name = "pages/price.html"

class LandinProductView(TemplateView):
    template_name = "pages/product.html"

class LandinPaymentView(TemplateView):
    template_name = "pages/payment.html"

class LandinTermsView(TemplateView):
    template_name = "pages/terms.html"


class LandinFaqsView(TemplateView):
    template_name = "pages/faqs.html"
