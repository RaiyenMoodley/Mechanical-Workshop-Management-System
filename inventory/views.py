from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Radiator
from .forms import RadiatorForm


@login_required
def radiator_list(request):
    """List all radiators"""
    radiators = Radiator.objects.all()
    return render(request, 'inventory/radiator_list.html', {'radiators': radiators})


@login_required
def radiator_create(request):
    """Create a new radiator"""
    if request.method == 'POST':
        form = RadiatorForm(request.POST)
        if form.is_valid():
            radiator = form.save()
            messages.success(request, f'{radiator.name} has been added to inventory successfully!')
            return redirect('inventory:radiator_list')
    else:
        form = RadiatorForm()
    return render(request, 'inventory/radiator_form.html', {'form': form, 'title': 'Add New Radiator'})


@login_required
def radiator_update(request, pk):
    """Update an existing radiator"""
    radiator = get_object_or_404(Radiator, pk=pk)
    if request.method == 'POST':
        form = RadiatorForm(request.POST, instance=radiator)
        if form.is_valid():
            radiator = form.save()
            messages.success(request, f'{radiator.name} has been updated successfully!')
            return redirect('inventory:radiator_list')
    else:
        form = RadiatorForm(instance=radiator)
    return render(request, 'inventory/radiator_form.html', {'form': form, 'radiator': radiator, 'title': 'Edit Radiator'})


@login_required
def radiator_delete(request, pk):
    """Delete a radiator"""
    radiator = get_object_or_404(Radiator, pk=pk)
    if request.method == 'POST':
        radiator_name = radiator.name
        radiator.delete()
        messages.success(request, f'{radiator_name} has been deleted from inventory successfully!')
        return redirect('inventory:radiator_list')
    return render(request, 'inventory/radiator_confirm_delete.html', {'radiator': radiator})
