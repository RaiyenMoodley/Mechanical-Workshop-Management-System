from django.db import models
from django.urls import reverse
from django.utils import timezone


class Booking(models.Model):
    """Model for booking vehicles or radiators"""
    
    BOOKING_TYPE_CHOICES = [
        ('vehicle', 'Vehicle'),
        ('radiator', 'Radiator'),
    ]
    
    WORK_TYPE_CHOICES = [
        ('repair', 'Repair'),
        ('service', 'Service'),
        ('radiator_replacement', 'Radiator Replacement'),
        ('other', 'Other'),
    ]
    
    PART_TYPE_CHOICES = [
        ('Radiator', 'Radiator'),
        ('Oil Cooler', 'Oil Cooler'),
        ('Intercooler', 'Intercooler'),
        ('Fuel Tank', 'Fuel Tank'),
        ('Other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    ALL_DAY_CHOICES = [
        (False, 'Hourly'),
        (True, 'All Day'),
    ]
    
    # Basic booking information
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE_CHOICES)
    customer_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    
    # Date and time
    booking_date = models.DateField()
    booking_time = models.TimeField(blank=True, null=True)  # Null if all_day is True
    all_day = models.BooleanField(default=False)
    
    # Conditional fields based on booking_type
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES, blank=True, null=True)  # For vehicles
    part_type = models.CharField(max_length=50, choices=PART_TYPE_CHOICES, blank=True, null=True)  # For radiators
    
    # Vehicle fields (for vehicle bookings)
    vehicle_make = models.CharField(max_length=100, blank=True, null=True, help_text="Vehicle make (e.g., Toyota, Ford)")
    vehicle_model = models.CharField(max_length=100, blank=True, null=True, help_text="Vehicle model (e.g., Corolla, Focus)")
    vehicle_registration = models.CharField(max_length=50, blank=True, null=True, help_text="Vehicle registration number")
    
    # Description (for radiator bookings)
    description = models.CharField(max_length=500, blank=True, null=True, help_text="Radiator/Part description")
    
    # Additional information
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Links to existing records (optional, linked by customer name)
    linked_job = models.ForeignKey('jobs.Job', on_delete=models.SET_NULL, blank=True, null=True, related_name='bookings')
    linked_radiator = models.ForeignKey('inventory.Radiator', on_delete=models.SET_NULL, blank=True, null=True, related_name='bookings')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['booking_date', 'booking_time']
    
    def __str__(self):
        booking_type_display = "Vehicle" if self.booking_type == 'vehicle' else "Radiator"
        time_display = "All Day" if self.all_day else self.booking_time.strftime("%H:%M")
        return f"{self.customer_name} - {booking_type_display} ({self.booking_date} {time_display})"
    
    def get_absolute_url(self):
        return reverse('bookings:booking_detail', kwargs={'pk': self.pk})
    
    def get_status_color(self):
        """Return color class for status"""
        colors = {
            'pending': 'status-orange',
            'confirmed': 'status-blue',
            'completed': 'status-green',
            'cancelled': 'status-red',
        }
        return colors.get(self.status, 'status-default')
    
    def get_booking_type_color(self):
        """Return color for calendar display based on booking type"""
        return '#667eea' if self.booking_type == 'vehicle' else '#48bb78'  # Purple for vehicle, green for radiator
