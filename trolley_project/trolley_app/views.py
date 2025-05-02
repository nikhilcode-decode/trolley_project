from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TrolleyChecklistForm
from .models import TrolleyChecklist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv

@login_required
def trolley_checklist_view(request):
    if request.method == 'POST':
        form = TrolleyChecklistForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            instance.user = request.user  # ✅ CORRECT
            values = [
                getattr(instance, field.name)
                for field in instance._meta.fields
                if field.name not in ['trolley_no', 'inspector_name', 'id', 'status', 'date_checked', 'user']
            ]
            instance.status = "OK" if all(val == "OK" for val in values) else "NG"
            instance.save()
            messages.success(request, "Thank you! Checklist submitted successfully!")
            return redirect('checklist')
    else:
        form = TrolleyChecklistForm()
    return render(request, 'trolley_checklist.html', {'form': form})

@login_required
def checklist_dashboard(request):
    checklists = TrolleyChecklist.objects.all()  # Get all checklists

    # Filter by logged-in user (optional)
    if request.user.is_authenticated:
        checklists = checklists.filter(user=request.user)

    return render(request, 'checklist_dashboard.html', {'checklists': checklists})

def export_trolley_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="trolley_checklist.csv"'

    writer = csv.writer(response)
    field_names = [f.name for f in TrolleyChecklist._meta.fields]
    writer.writerow(field_names)

    for obj in TrolleyChecklist.objects.all():
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

