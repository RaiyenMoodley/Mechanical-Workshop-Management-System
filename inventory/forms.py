from django import forms
from .models import Radiator


class RadiatorForm(forms.ModelForm):
    """Form for creating and updating parts orders"""
    
    class Meta:
        model = Radiator
        fields = [
            'name',
            'part_type',
            'customer_name',
            'contact_number',
            'status',
            'notes',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter radiator/part name/model'
            }),
            'part_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Additional notes (optional)'
            }),
        }
