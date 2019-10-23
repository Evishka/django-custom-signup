from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = 'home.html'

