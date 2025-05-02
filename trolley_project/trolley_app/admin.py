from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TrolleyChecklist

@admin.register(TrolleyChecklist)
class TrolleyChecklistAdmin(admin.ModelAdmin):
    list_display = ['trolley_no', 'status', 'date_checked','inspector_name']
    list_filter = ['status', 'date_checked']
    search_fields = ['trolley_no']

