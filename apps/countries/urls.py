from django.urls import path
from apps.countries import views


urlpatterns = [
   path('', views.CountriesIndexView.as_view(), name='country_index'),
   path('country/<str:slug>/', views.CountriesDetailView.as_view(), name='country_detail'),
   path('create/', views.CountriesCreateView.as_view(), name='country_create'),
]