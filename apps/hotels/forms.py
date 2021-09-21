from django import forms
from apps.hotels.models import Hotel, HotelImage
from django.forms import ModelForm


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        exclude = []
        fields = ['title', 'description', 'price', 'countries', 'wifi', 'parking']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'countries': forms.Select(attrs={'class': 'form-control'}),
            'wifi': forms.Select(attrs={'class': "form-control"}),
            'parking': forms.Select(attrs={'class': "form-control"}),
        }

class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }