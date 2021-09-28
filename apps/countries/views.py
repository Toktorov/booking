from django.shortcuts import render, redirect
from apps.countries.models import Country, CountryImage
from apps.countries.forms import CountryForm, CountryImageForm
from django.forms import inlineformset_factory
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class CountriesIndexView(generic.ListView):
    model = Country
    template_name = 'countries/index.html'
    context_object_name = 'countries'

    def get_queryset(self):
        queryset = Country.objects.all()
        qury_obj = self.request.GET.get('words')
        if qury_obj:
            queryset = Country.objects.filter(
                Q(title__icontains=qury_obj)
            )
        return queryset

class CountriesDetailView(generic.DetailView):
    model = Country
    template_name = 'countries/detail.html'
    context_object_name = 'country'

class CountriesCreateView(generic.CreateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country_index')
    template_name = 'countries/create.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CountriesUpdateView(generic.UpdateView):
    model = Country
    form_class = CountryForm
    success_url = reverse_lazy('country_index')
    template_name = 'countries/update.html'

class CountriesDeleteView(generic.DeleteView):
    model = Country
    success_url = reverse_lazy('country_index')
    template_name = 'countries/delete.html'