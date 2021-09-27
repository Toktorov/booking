from django.urls import path
from apps.tags import views

urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='tag_create'),
    path('update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete'),
]