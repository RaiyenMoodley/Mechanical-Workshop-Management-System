from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'vehicle_registration', 'vehicle_make', 'vehicle_model', 'work_type', 'status', 'invoice_number', 'date_received', 'date_completed']
    list_filter = ['status', 'work_type', 'date_received']
    search_fields = ['customer_name', 'vehicle_registration', 'vehicle_make', 'vehicle_model', 'invoice_number']
    date_hierarchy = 'date_received'
    ordering = ['-created_at']
