from django.shortcuts import render
from django.views.generic import ListView
from base.models import Item


class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'
