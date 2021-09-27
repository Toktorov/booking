from django import forms
from apps.hotels.models import Hotel, HotelImage
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        extra = 1
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        exclude = []
        inlines = [HotelImageForm]
        fields = ['title', 'description', 'price', 'payment', 'wifi', 'parking', 'front_desk', 
        'family_rooms', 'non_smoking_rooms', 'contact_number', 'tags', 'countries']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
            'wifi': forms.Select(attrs={'class': "form-control"}),
            'parking': forms.Select(attrs={'class': "form-control"}),
            'front_desk': forms.Select(attrs={'class': "form-control"}),
            'family_rooms': forms.Select(attrs={'class': "form-control"}),
            'non_smoking_rooms': forms.Select(attrs={'class': "form-control"}),
            'contact_number': forms.TextInput(attrs={'class': "form-control"}),
            'tags': forms.Select(attrs={'class': "form-control"}),
            'countries': forms.Select(attrs={'class': 'form-control'}),
        }
