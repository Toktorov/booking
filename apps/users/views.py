from django.shortcuts import render
from apps.users.models import User
from apps.users.forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def profile(request, username):
    users = User.objects.get(username=username)
    context = {
       "user": users,
    }
    return render(request, 'registration/profile.html', context)