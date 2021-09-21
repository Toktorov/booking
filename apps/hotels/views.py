from django.shortcuts import render, redirect
from apps.hotels.models import Hotel, HotelImage, Like
from apps.hotels.forms import HotelForm, HotelImageForm
from apps.comments.models import Comment
from apps.comments.forms import CommentForm
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
class HotelsIndexView(ListView):
    model = Hotel
    template_name = 'hotels/index.html'
    context_object_name = 'hotels'

def detail_hotel(request, pk):
    hotels = Hotel.objects.get()
    if 'like' in request.POST:
        try:
            like = Like.objects.get(user=request.user, hotels=hotels)
            like.delete()
        except:
            Like.objects.create(user=request.user, hotels=hotels)
    
    if 'comment' in request.POST:
        try:
            text = request.POST.get('text')
            comment_obj = Comment.objects.create(user=request.user, hotel=hotels, text=text)
            return redirect('detail', hotel.pk)
        except:
            print("Error")
    return render(request, 'hotels/detail.html', {"hotel": hotels})

class HotelCreateView(CreateView):
    model = Hotel
    fields = ['title', 'description', 'price', 'countries', 'wifi', 'parking']
    success_url = reverse_lazy('hotel_index')
    template_name = 'hotels/create.html'