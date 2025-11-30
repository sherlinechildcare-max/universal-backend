from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'caregiver', 'date', 'start_time', 'end_time', 'status')
    list_filter = ('date', 'status')
    search_fields = ('client__username', 'caregiver__username', 'location', 'status')