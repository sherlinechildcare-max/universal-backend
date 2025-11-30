from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'caregiver', 'amount', 'status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('client__username', 'caregiver__username', 'status')