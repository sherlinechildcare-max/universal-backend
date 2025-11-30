from django.db import models
from users.models import CustomUser

class Job(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='client_jobs')
    caregiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='caregiver_jobs')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='pending')  # accepted, cancelled, completed
    gps_log = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Job: {self.client} → {self.caregiver} on {self.date}"