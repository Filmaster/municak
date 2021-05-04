from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return render(request, template_name='index.html')


class ProduktListView(ListView):
    model = Prukaz
    context_object_name = 'produkt_list'
    template_name = 'list.html'


class ProduktDetailView(DetailView):
    model = Prukaz
    context_object_name = 'produkt'
    template_name = 'detail.html'


