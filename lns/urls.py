from django.urls import reverse, path
from . import views

urlpatterns = [
    path("", views.LandinHomeView.as_view(), name="home"),
    path("about/", views.LandinAboutView.as_view(), name="about"),
    path("contact-us/", views.LandinContactView.as_view(), name="contact"),
    path("pricing-plans/", views.LandinPricingView.as_view(), name="pricing"),
    path("frequently-asked-questions/", views.LandinFaqsView.as_view(), name="faqs"),
]
