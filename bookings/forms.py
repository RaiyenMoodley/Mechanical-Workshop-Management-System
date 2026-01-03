from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for creating and updating bookings"""
    
    class Meta:
        model = Booking
        fields = [
            'booking_type',
            'customer_name',
            'contact_number',
            'booking_date',
            'all_day',
            'booking_time',
            'work_type',
            'part_type',
            'vehicle_make',
            'vehicle_model',
            'description',
            'notes',
            'status',
        ]
        widgets = {
            'booking_type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_booking_type',
                'onchange': 'toggleBookingFields()'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
            'booking_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'all_day': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'id_all_day',
                'onchange': 'toggleTimeField()'
            }),
            'booking_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'id': 'id_booking_time'
            }),
            'work_type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_work_type'
            }),
            'part_type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_part_type'
            }),
            'vehicle_make': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_vehicle_make',
                'placeholder': 'Enter vehicle make (e.g., Toyota, Ford)'
            }),
            'vehicle_model': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_vehicle_model',
                'placeholder': 'Enter vehicle model (e.g., Corolla, Focus)'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_description',
                'placeholder': 'Enter radiator/part description'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Additional notes (optional)'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial visibility based on booking_type
        if self.instance and self.instance.pk:
            if self.instance.booking_type == 'vehicle':
                self.fields['work_type'].required = True
                self.fields['part_type'].required = False
                self.fields['description'].required = False
                self.fields['vehicle_make'].required = True
                self.fields['vehicle_model'].required = True
            elif self.instance.booking_type == 'radiator':
                self.fields['work_type'].required = False
                self.fields['part_type'].required = True
                self.fields['description'].required = True
                self.fields['vehicle_make'].required = False
                self.fields['vehicle_model'].required = False
        else:
            # For new bookings, make both optional initially
            self.fields['work_type'].required = False
            self.fields['part_type'].required = False
            self.fields['description'].required = False
            self.fields['vehicle_make'].required = False
            self.fields['vehicle_model'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        booking_type = cleaned_data.get('booking_type')
        all_day = cleaned_data.get('all_day')
        booking_time = cleaned_data.get('booking_time')
        work_type = cleaned_data.get('work_type')
        part_type = cleaned_data.get('part_type')
        
        # Validate time field based on all_day
        if not all_day and not booking_time:
            raise forms.ValidationError("Booking time is required when not selecting 'All Day'.")
        
        if all_day:
            cleaned_data['booking_time'] = None
        
        # Validate conditional fields based on booking_type
        vehicle_make = cleaned_data.get('vehicle_make')
        vehicle_model = cleaned_data.get('vehicle_model')
        description = cleaned_data.get('description')
        
        if booking_type == 'vehicle':
            if not work_type:
                raise forms.ValidationError("Work type is required for vehicle bookings.")
            if not vehicle_make:
                raise forms.ValidationError("Vehicle make is required for vehicle bookings.")
            if not vehicle_model:
                raise forms.ValidationError("Vehicle model is required for vehicle bookings.")
            cleaned_data['part_type'] = None
            cleaned_data['description'] = None
        elif booking_type == 'radiator':
            if not part_type:
                raise forms.ValidationError("Part type is required for radiator bookings.")
            if not description:
                raise forms.ValidationError("Description is required for radiator bookings.")
            cleaned_data['work_type'] = None
            cleaned_data['vehicle_make'] = None
            cleaned_data['vehicle_model'] = None
        
        return cleaned_data

