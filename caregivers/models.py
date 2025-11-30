from django.db import models
from users.models import CustomUser

class CaregiverProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    certifications = models.TextField()
    video_resume_url = models.URLField(blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    badges = models.JSONField(default=list)  # e.g. ["Dementia", "CPR"]
    care_score = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.username}'s Profile"