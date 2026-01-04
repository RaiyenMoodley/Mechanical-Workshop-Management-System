from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime, date
from .models import Booking
from .forms import BookingForm
from jobs.models import Job
from inventory.models import Radiator


@login_required
def booking_list(request):
    """List all bookings"""
    bookings = Booking.objects.all().order_by('booking_date', 'booking_time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_calendar(request):
    """Display calendar view of bookings"""
    return render(request, 'bookings/booking_calendar.html')


@login_required
def booking_events_api(request):
    """API endpoint to return bookings as JSON for FullCalendar"""
    start = request.GET.get('start')
    end = request.GET.get('end')
    
    bookings = Booking.objects.all()
    
    if start:
        try:
            # Handle ISO format with or without timezone
            start_str = start.replace('Z', '+00:00') if 'Z' in start else start
            start_date = datetime.fromisoformat(start_str).date()
            bookings = bookings.filter(booking_date__gte=start_date)
        except (ValueError, AttributeError):
            pass
    
    if end:
        try:
            # Handle ISO format with or without timezone
            end_str = end.replace('Z', '+00:00') if 'Z' in end else end
            end_date = datetime.fromisoformat(end_str).date()
            bookings = bookings.filter(booking_date__lte=end_date)
        except (ValueError, AttributeError):
            pass
    
    events = []
    for booking in bookings:
        # Determine start datetime
        if booking.all_day:
            start_datetime = datetime.combine(booking.booking_date, datetime.min.time())
            end_datetime = datetime.combine(booking.booking_date, datetime.max.time())
            all_day = True
        else:
            start_datetime = datetime.combine(booking.booking_date, booking.booking_time)
            # Default to 1 hour duration if not all day
            from datetime import timedelta
            end_datetime = start_datetime + timedelta(hours=1)
            all_day = False
        
        # Get color based on booking type
        color = booking.get_booking_type_color()
        
        # Create title
        booking_type_label = "Vehicle" if booking.booking_type == 'vehicle' else "Radiator"
        if booking.booking_type == 'vehicle' and booking.vehicle_make and booking.vehicle_model:
            title = f"{booking.customer_name} - {booking.vehicle_make} {booking.vehicle_model}"
        elif booking.booking_type == 'radiator' and booking.description:
            title = f"{booking.customer_name} - {booking.description[:30]}"
        else:
            title = f"{booking.customer_name} - {booking_type_label}"
        
        events.append({
            'id': booking.pk,
            'title': title,
            'start': start_datetime.isoformat(),
            'end': end_datetime.isoformat(),
            'allDay': all_day,
            'color': color,
            'extendedProps': {
                'booking_type': booking.booking_type,
                'customer_name': booking.customer_name,
                'contact_number': booking.contact_number,
                'description': booking.description,
                'vehicle_make': booking.vehicle_make,
                'vehicle_model': booking.vehicle_model,
                'status': booking.status,
                'notes': booking.notes,
            }
        })
    
    return JsonResponse(events, safe=False)


@login_required
def booking_detail(request, pk):
    """View details of a specific booking"""
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})


@login_required
def booking_create(request):
    """Create a new booking and optionally create linked Job/Radiator"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            
            # Try to link to existing records by customer name
            if booking.booking_type == 'vehicle':
                # Try to find matching job
                matching_job = Job.objects.filter(
                    customer_name__iexact=booking.customer_name
                ).order_by('-created_at').first()
                if matching_job:
                    booking.linked_job = matching_job
            
            elif booking.booking_type == 'radiator':
                # Try to find matching radiator
                matching_radiator = Radiator.objects.filter(
                    customer_name__iexact=booking.customer_name
                ).order_by('-created_at').first()
                if matching_radiator:
                    booking.linked_radiator = matching_radiator
            
            booking.save()
            
            # Create Job or Radiator record
            if booking.booking_type == 'vehicle':
                # Create Job record using vehicle fields (vehicle_registration will be "TBD" since it's not in booking)
                job = Job.objects.create(
                    customer_name=booking.customer_name,
                    contact_number=booking.contact_number,
                    vehicle_registration="TBD",  # Not collected in booking form
                    vehicle_make=booking.vehicle_make,
                    vehicle_model=booking.vehicle_model,
                    work_type=booking.work_type,
                    status='Pending',
                    date_received=booking.booking_date,  # Set date_received to booking date
                    notes=booking.notes,
                )
                booking.linked_job = job
                booking.save()
                messages.success(request, f'Booking and Job for {booking.customer_name} have been created successfully!')
            else:
                # Create Radiator record
                radiator = Radiator.objects.create(
                    name=booking.description,
                    part_type=booking.part_type,
                    customer_name=booking.customer_name,
                    contact_number=booking.contact_number,
                    status='Pending',
                    notes=booking.notes,
                )
                booking.linked_radiator = radiator
                booking.save()
                messages.success(request, f'Booking and Radiator order for {booking.customer_name} have been created successfully!')
            
            return redirect('bookings:booking_calendar')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'title': 'Create New Booking'})


@login_required
def booking_update(request, pk):
    """Update an existing booking"""
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f'Booking for {booking.customer_name} has been updated successfully!')
            return redirect('bookings:booking_calendar')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'booking': booking, 'title': 'Edit Booking'})


@login_required
def booking_delete(request, pk):
    """Delete a booking"""
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        customer_name = booking.customer_name
        booking.delete()
        messages.success(request, f'Booking for {customer_name} has been deleted successfully!')
        return redirect('bookings:booking_calendar')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})
