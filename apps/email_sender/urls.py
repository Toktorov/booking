from django.urls import path
from apps.email_sender.views import MessageSenderCreateView


urlpatterns = [
    path('', MessageSenderCreateView.as_view(), name='send_sms'),
]