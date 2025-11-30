from django.contrib import admin
from .models import CaregiverProfile

@admin.register(CaregiverProfile)
class CaregiverProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'experience_years')  # replace with actual fields
