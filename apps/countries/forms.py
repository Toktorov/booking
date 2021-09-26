from django import forms
from apps.countries.models import Country, CountryImage


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.TextInput(attrs={'class': "form-control"}),
        }
    
class CountryImageForm(forms.ModelForm):
    class Meta:
        model = CountryImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }