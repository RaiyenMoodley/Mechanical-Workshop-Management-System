from django.db import models
from django.urls import reverse
from django.utils import timezone


class Radiator(models.Model):
    """Model for tracking parts orders (Radiators, Intercoolers, Fuel Tanks)"""
    
    PART_TYPE_CHOICES = [
        ('Radiator', 'Radiator'),
        ('Intercooler', 'Intercooler'),
        ('Fuel Tank', 'Fuel Tank'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=200, help_text="Radiator Name/Model")
    part_type = models.CharField(max_length=50, choices=PART_TYPE_CHOICES, default='Radiator')
    customer_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_received = models.DateField(auto_now_add=True)
    date_completed = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.customer_name} ({self.status})"
    
    def get_absolute_url(self):
        return reverse('inventory:radiator_list')
    
    def save(self, *args, **kwargs):
        """Override save to automatically set date_completed when status changes to Completed"""
        if self.status == 'Completed' and not self.date_completed:
            self.date_completed = timezone.now().date()
        elif self.status != 'Completed':
            self.date_completed = None
        super().save(*args, **kwargs)
    
    def get_status_color(self):
        """Return color class for status"""
        colors = {
            'Pending': 'status-red',
            'In Progress': 'status-orange',
            'Completed': 'status-green',
        }
        return colors.get(self.status, 'status-default')
