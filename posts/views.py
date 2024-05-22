from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PostDetailView(TemplateView):
    template_name = "posts/detail.html"