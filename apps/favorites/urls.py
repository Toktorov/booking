from django.urls import path
from apps.favorites import views


urlpatterns = [
    path('', views.FavoriteIndexView.as_view(), name='favorite_index'),
]