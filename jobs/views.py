from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job
from .forms import JobForm


@login_required
def job_list(request):
    """List all jobs, most recent first"""
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


@login_required
def job_detail(request, pk):
    """View details of a specific job"""
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def job_create(request):
    """Create a new job"""
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, f'Job for {job.customer_name} has been created successfully!')
            return redirect('jobs:job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form, 'title': 'Add New Job'})


@login_required
def job_update(request, pk):
    """Update an existing job"""
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save()
            messages.success(request, f'Job for {job.customer_name} has been updated successfully!')
            return redirect('jobs:job_detail', pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form, 'job': job, 'title': 'Edit Job'})


@login_required
def job_delete(request, pk):
    """Delete a job"""
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        customer_name = job.customer_name
        job.delete()
        messages.success(request, f'Job for {customer_name} has been deleted successfully!')
        return redirect('jobs:job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})
