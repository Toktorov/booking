from django.urls import path 
from apps.transactions import views


urlpatterns = [
    path('detail/<int:payment_id>/', views.payment_details, name = 'detail_payments'),
]