from django.urls import path
from apps.orders import views


urlpatterns = [
   path('', views.OrderIndexView.as_view(), name='order_index'),
   path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
   path('create/', views.OrderCreateView.as_view(), name='order_create'),
   path('update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
   path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
   path('success/', views.successmessage, name = 'success_message')
]