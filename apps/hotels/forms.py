from django import forms
from apps.hotels.models import Hotel, HotelImage
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        exclude = []
        fields = ['title', 'description', 'price', 'payment', 'wifi', 'parking', 'front_desk', 
        'family_rooms', 'non_smoking_rooms', 'contact_number', 'countries']
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
            'countries': forms.Select(attrs={'class': 'form-control'}),
        }
        HotelImageFormSet = inlineformset_factory(Hotel, HotelImage,
                                            form=HotelImageForm, extra=2)
