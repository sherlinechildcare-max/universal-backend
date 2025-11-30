from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('caregiver', 'Caregiver'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    # Useful for filtering
    is_caregiver = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"