from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class Index(generic.TemplateView):
    template_name = "home/index.html"

class Pricing(generic.TemplateView):
    template_name = "home/pricing.html"
