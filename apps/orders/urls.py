from django.urls import path
from apps.orders import views


urlpatterns = [
   path('', views.OrderIndexView.as_view(), name='order_index'),
   path('order/<int:order_pk>/', views.OrderDetailView.as_view(), name='order_detail'),
   path('create/', views.OrderCreateView.as_view(), name='order_create'),
   path('success/', views.successmessage, name = 'success_message')
]