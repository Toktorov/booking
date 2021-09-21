from django.urls import path
from apps.hotels import views


urlpatterns = [
   path('', views.HotelsIndexView.as_view(), name='hotel_index'),
   path('hotel/<int:pk>/', views.detail_hotel, name='hotel_detail'),
   path('create/', views.HotelCreateView.as_view(), name='hotel_create'),
]