from apps.users.models import User
from django import  forms
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'profile', 'phone_number', 'age',
            'gender',
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'profile': forms.FileInput(attrs={'class': "form-control"}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }