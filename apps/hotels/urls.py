from django.urls import path
from apps.hotels import views


urlpatterns = [
   path('', views.HotelsIndexView.as_view(), name='hotel_index'),
   path('hotel/<int:pk>/', views.detail_hotel, name='hotel_detail'),
   path('create/', views.HotelCreateView.as_view(), name='hotel_create'),
   path('map/', views.map, name='map'),
   path('about_us/', views.about_us, name='about_us'),
   path('update/<int:pk>/', views.HotelUpdateView.as_view(), name='hotel_update'),
   path('delete/<int:pk>/', views.HotelDeleteView.as_view(), name='hotel_delete'),
]