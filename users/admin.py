from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_caregiver', 'is_patient', 'is_active')
    list_filter = ('role', 'is_caregiver', 'is_patient', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone', 'language', 'location', 'is_caregiver', 'is_patient')}),
    )
    search_fields = ('username', 'email', 'role', 'phone')