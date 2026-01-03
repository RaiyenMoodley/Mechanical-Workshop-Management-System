from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """Form for creating and updating jobs"""
    
    class Meta:
        model = Job
        fields = [
            'customer_name',
            'contact_number',
            'vehicle_registration',
            'vehicle_make',
            'vehicle_model',
            'work_type',
            'status',
            'invoice_number',
            'notes',
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
            'vehicle_registration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vehicle registration'
            }),
            'vehicle_make': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Toyota, Ford'
            }),
            'vehicle_model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Corolla, Focus'
            }),
            'work_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'invoice_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter invoice number (optional)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Additional notes (optional)'
            }),
        }

