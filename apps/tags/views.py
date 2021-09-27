from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from apps.tags.models import Tag
from apps.tags.forms import TagForm

# Create your views here.
class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('country_index')
    template_name = 'tags/create.html'

class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('country_index')
    template_name = 'tags/update.html'

class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('country_index')
    template_name = 'tags/delete.html'