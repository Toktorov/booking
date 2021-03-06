from django import forms
from apps.orders.models import Order
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'

class OrderForm(ModelForm):
    class Meta:
        model = Order 
        fields = ['arrival_date', 'departure_date', 'name', 'surname', 'fatherland', 'id_card', 'contact_number']
        widgets = {
            'arrival_date': DateInput(attrs={'class': "form-control"}, ),
            'departure_date': DateInput(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'surname': forms.TextInput(attrs={'class': "form-control"}),
            'fatherland': forms.TextInput(attrs={'class': "form-control"}),
            'id_card': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderAdminForm(ModelForm):
    class Meta:
        model = Order 
        fields = ['arrival_date', 'departure_date', 'name', 'surname', 'fatherland', 'id_card', 'contact_number', 'status']
        widgets = {
            'arrival_date': DateInput(attrs={'class': "form-control"}, ),
            'departure_date': DateInput(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'surname': forms.TextInput(attrs={'class': "form-control"}),
            'fatherland': forms.TextInput(attrs={'class': "form-control"}),
            'id_card': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }