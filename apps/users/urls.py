from django.urls import path
from apps.users.views import UserCreateView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
]