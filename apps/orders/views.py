from django.shortcuts import render, redirect
from apps.orders.models import Order
from apps.orders.forms import OrderForm
from django.forms import inlineformset_factory
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.urls import reverse

# Create your views here.
class OrderIndexView(generic.ListView):
    model = Order
    template_name = 'order/index.html'
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = 'order'

class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/create.html'

    def get_success_url(self):
        return reverse("country_index")
