from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class Index(generic.TemplateView):
    #template_name = "content/index.html"
    template_name = "base.html"
