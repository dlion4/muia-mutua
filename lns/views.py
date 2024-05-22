from django.shortcuts import render
from django.views.generic import TemplateView


class LandinHomeView(TemplateView):
    template_name = "pages/home.html"


class LandinAboutView(TemplateView):
    template_name = "pages/about.html"


class LandinContactView(TemplateView):
    template_name = "pages/contact.html"


class LandinPricingView(TemplateView):
    template_name = "pages/price.html"


class LandinFaqsView(TemplateView):
    template_name = "pages/faqs.html"

