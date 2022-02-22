from django.urls import path
from apps.countries import views


urlpatterns = [
   path('', views.CountriesIndexView.as_view(), name='country_index'),
   path('city/<str:slug>/', views.CountriesDetailView.as_view(), name='country_detail'),
   path('create/', views.CountriesCreateView.as_view(), name='country_create'),
   path('update/<str:slug>/', views.CountriesUpdateView.as_view(), name='country_update'),
   path('delete/<str:slug>/', views.CountriesDeleteView.as_view(), name='country_delete'),
]