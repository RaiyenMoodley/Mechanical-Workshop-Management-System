from django.db import models
from django.urls import reverse
from decimal import Decimal


class Radiator(models.Model):
    """Model for tracking radiator inventory"""
    
    name = models.CharField(max_length=200)
    compatible_vehicles = models.TextField(help_text="List of compatible vehicles")
    quantity = models.IntegerField(default=0)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"
    
    def get_absolute_url(self):
        return reverse('inventory:radiator_list')
    
    def is_low_stock(self):
        """Check if stock is low (quantity < 5)"""
        return self.quantity < 5
    
    def get_profit_margin(self):
        """Calculate profit margin"""
        if self.cost_price > 0:
            return self.selling_price - self.cost_price
        return Decimal('0.00')
