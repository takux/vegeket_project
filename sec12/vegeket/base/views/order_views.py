from django.views.generic import ListView, DetailView
from base.models import Order
import json
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderIndexView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'pages/order.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        # json to dict
        context["items"] = json.loads(obj.items)
        context["shipping"] = json.loads(obj.shipping)
        return context
