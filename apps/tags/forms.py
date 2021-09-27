from django import forms
from apps.tags.models import Tag
from django.forms import ModelForm

class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = []
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
        }