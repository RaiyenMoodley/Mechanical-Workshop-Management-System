from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Radiator
from .forms import RadiatorForm


@login_required
def radiator_list(request):
    """List all parts orders"""
    radiators = Radiator.objects.all()
    return render(request, 'inventory/radiator_list.html', {'radiators': radiators})


@login_required
def radiator_create(request):
    """Create a new parts order"""
    if request.method == 'POST':
        form = RadiatorForm(request.POST)
        if form.is_valid():
            radiator = form.save()
            messages.success(request, f'Parts order for {radiator.customer_name} has been created successfully!')
            return redirect('inventory:radiator_list')
    else:
        form = RadiatorForm()
    return render(request, 'inventory/radiator_form.html', {'form': form, 'title': 'Add New Parts Order'})


@login_required
def radiator_update(request, pk):
    """Update an existing parts order"""
    radiator = get_object_or_404(Radiator, pk=pk)
    if request.method == 'POST':
        form = RadiatorForm(request.POST, instance=radiator)
        if form.is_valid():
            radiator = form.save()
            messages.success(request, f'Parts order for {radiator.customer_name} has been updated successfully!')
            return redirect('inventory:radiator_list')
    else:
        form = RadiatorForm(instance=radiator)
    return render(request, 'inventory/radiator_form.html', {'form': form, 'radiator': radiator, 'title': 'Edit Parts Order'})


@login_required
def radiator_delete(request, pk):
    """Delete a parts order"""
    radiator = get_object_or_404(Radiator, pk=pk)
    if request.method == 'POST':
        customer_name = radiator.customer_name
        radiator.delete()
        messages.success(request, f'Parts order for {customer_name} has been deleted successfully!')
        return redirect('inventory:radiator_list')
    return render(request, 'inventory/radiator_confirm_delete.html', {'radiator': radiator})
