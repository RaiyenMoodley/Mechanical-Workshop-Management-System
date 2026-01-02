from django.db import models
from django.urls import reverse


class Job(models.Model):
    """Model for tracking workshop jobs (cars coming in)"""
    
    WORK_TYPE_CHOICES = [
        ('repair', 'Repair'),
        ('service', 'Service'),
        ('radiator_replacement', 'Radiator Replacement'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    customer_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    vehicle_registration = models.CharField(max_length=50)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    work_type = models.CharField(max_length=50, choices=WORK_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_received = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
    
    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_registration} ({self.status})"
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})
    
    def get_status_color(self):
        """Return color class for status"""
        colors = {
            'Pending': 'status-red',
            'In Progress': 'status-orange',
            'Completed': 'status-green',
        }
        return colors.get(self.status, 'status-default')
