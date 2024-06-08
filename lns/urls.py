from django.urls import reverse, path
from . import views

urlpatterns = [
    path("", views.LandinHomeView.as_view(), name="home"),
    path("about/", views.LandinAboutView.as_view(), name="about"),
    path("contact-us/", views.LandinContactView.as_view(), name="contact"),
    path("pricing-plans/", views.LandinPricingView.as_view(), name="pricing"),
    path("product/", views.LandinProductView.as_view(), name="product"),
    path("payment/", views.LandinPaymentView.as_view(), name="payment"),
    path("terms/", views.LandinTermsView.as_view(), name="terms"),
    path("frequently-asked-questions/", views.LandinFaqsView.as_view(), name="faqs"),
]
