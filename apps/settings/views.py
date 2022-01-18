from django.shortcuts import render
from apps.settings.models import Setting

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk = 1)
    context = {
        'setting' : setting
    }
    return render(request, 'countries/index.html', context)