from django.shortcuts import render
from apps.favorites.models import Favorite
from django.views import generic

# Create your views here.
class FavoriteIndexView(generic.ListView):
    model = Favorite
    template_name = 'favorites/index.html'
    context_object_name = 'favorites'
