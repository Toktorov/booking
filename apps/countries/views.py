from django.shortcuts import render, redirect
from apps.countries.models import Country
from apps.countries.forms import CountryForm
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView

# Create your views here.
class CountriesIndexView(ListView):
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

class CountriesDetailView(DetailView):
    model = Country
    template_name = 'countries/detail.html'
    context_object_name = 'country'