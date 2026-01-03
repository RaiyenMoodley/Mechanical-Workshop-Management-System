from django.contrib import admin
from .models import Radiator


@admin.register(Radiator)
class RadiatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_type', 'customer_name', 'contact_number', 'status', 'date_received', 'date_completed']
    list_filter = ['status', 'part_type', 'date_received']
    search_fields = ['name', 'customer_name', 'contact_number']
    date_hierarchy = 'date_received'
    ordering = ['-created_at']
