from django import forms
from .models import Employee, Absence


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['employee', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

