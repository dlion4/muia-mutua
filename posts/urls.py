from django.urls import reverse, path
from . import views

app_name = "posts"
urlpatterns = [
    path("<pk>/", views.PostDetailView.as_view(), name="post"),
]
