from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Item


class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'
