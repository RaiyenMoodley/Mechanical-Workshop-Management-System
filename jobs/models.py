from django.db import models
from django.urls import reverse
from django.utils import timezone


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
    invoice_number = models.CharField(max_length=100, blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
    
    def save(self, *args, **kwargs):
        """Override save to automatically set date_completed when status changes to Completed"""
        if self.status == 'Completed' and not self.date_completed:
            self.date_completed = timezone.now().date()
        elif self.status != 'Completed':
            self.date_completed = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.customer_name} - {self.vehicle_registration} ({self.status})"
    
    def get_absolute_url(self):
        return reverse('jobs:job_detail', kwargs={'pk': self.pk})
    
    def get_status_color(self):
        """Return color class for status"""
        colors = {
            'Pending': 'status-red',
            'In Progress': 'status-orange',
            'Completed': 'status-green',
        }
        return colors.get(str(self.status), 'status-default')
