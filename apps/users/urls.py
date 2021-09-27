from django.urls import path
from apps.users.views import UserCreateView, profile

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('profile/<username>', profile, name='profile'),
]