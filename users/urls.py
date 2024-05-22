from django.urls import reverse, path, include
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="signup"),
]
