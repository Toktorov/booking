from django.shortcuts import render, redirect
from apps.orders.models import Order
from apps.orders.forms import OrderForm
from django.views import generic
from django.urls import reverse_lazy
from apps.hotels.models import Hotel

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
    success_url = reverse_lazy('success_message')
    template_name = 'order/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateView, self).form_valid(form)

class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_index')
    template_name = 'order/update.html'

class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('order_index')
    template_name = 'order/delete.html'


def successmessage(request):
    return render(request, 'order/success.html')
