from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AbsenceForm, EmployeeForm
from .models import Absence, Employee


@login_required
def absence_calendar(request):
    """Calendar view for absentees (similar to booking calendar)."""
    employees = Employee.objects.all().order_by('name')
    return render(
        request,
        'absentees/absence_calendar.html',
        {'employees': employees},
    )


@login_required
def absence_events_api(request):
    """Return absences as JSON for FullCalendar."""
    start = request.GET.get('start')
    end = request.GET.get('end')

    absences = Absence.objects.all()

    if start:
        try:
            start_str = start.replace('Z', '+00:00') if 'Z' in start else start
            start_date = datetime.fromisoformat(start_str).date()
            absences = absences.filter(date__gte=start_date)
        except (ValueError, AttributeError):
            pass

    if end:
        try:
            end_str = end.replace('Z', '+00:00') if 'Z' in end else end
            end_date = datetime.fromisoformat(end_str).date()
            absences = absences.filter(date__lte=end_date)
        except (ValueError, AttributeError):
            pass

    events = []
    for absence in absences:
        # All-day event for the absence date
        start_datetime = datetime.combine(absence.date, datetime.min.time())
        end_datetime = datetime.combine(absence.date, datetime.max.time())

        events.append(
            {
                'id': absence.pk,
                'title': absence.employee.name,
                'start': start_datetime.isoformat(),
                'end': end_datetime.isoformat(),
                'allDay': True,
                # Red legend for absences
                'color': '#e53e3e',
                'extendedProps': {
                    'employee_id': absence.employee_id,
                    'notes': absence.notes,
                },
            }
        )

    return JsonResponse(events, safe=False)


@login_required
def absence_create(request):
    """Create a new absence entry."""
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence = form.save()
            messages.success(
                request,
                f'{absence.employee.name} has been marked absent on {absence.date}.',
            )
            return redirect('absentees:absence_calendar')
    else:
        form = AbsenceForm()

    return render(
        request,
        'absentees/absence_form.html',
        {'form': form, 'title': 'Mark Employee Absent'},
    )


@login_required
def employee_list(request):
    """List employees with simple absence counts."""
    employees = (
        Employee.objects.annotate(absence_count=Count('absences'))
        .all()
        .order_by('name')
    )
    return render(
        request,
        'absentees/employee_list.html',
        {'employees': employees},
    )


@login_required
def employee_create(request):
    """Add a new employee."""
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'Employee {employee.name} has been added.')
            return redirect('absentees:employee_list')
    else:
        form = EmployeeForm()

    return render(
        request,
        'absentees/employee_form.html',
        {'form': form, 'title': 'Add Employee'},
    )


@login_required
def employee_delete(request, pk):
    """Delete an employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        name = employee.name
        employee.delete()
        messages.success(request, f'Employee {name} has been deleted.')
        return redirect('absentees:employee_list')

    return render(
        request,
        'absentees/employee_confirm_delete.html',
        {'employee': employee},
    )


@login_required
def employee_detail(request, pk):
    """Show absence statistics for a single employee."""
    employee = get_object_or_404(Employee, pk=pk)
    absences = employee.absences.all().order_by('date')
    total_absences = absences.count()

    return render(
        request,
        'absentees/employee_detail.html',
        {
            'employee': employee,
            'absences': absences,
            'total_absences': total_absences,
        },
    )

