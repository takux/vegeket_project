from django.shortcuts import render
from django.views.generic import ListView, DetailView
from base.models import Item, Category, Tag


class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'pages/item.html'


class CategoryListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 2

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['pk'])
        self.queryset = Item.objects.filter(
            is_published=True, category=self.category)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Category #{self.category.name}"
        return context


class TagListView(ListView):
    model = Item
    template_name = 'pages/list.html'
    paginate_by = 2

    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        self.queryset = Item.objects.filter(is_published=True, tags=self.tag)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Tag #{self.tag.name}"
        return context
