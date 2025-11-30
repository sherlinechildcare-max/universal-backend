from django.db import models
from users.models import CustomUser

class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    medical_conditions = models.JSONField(default=list)
    care_preferences = models.JSONField(default=dict)  # e.g. {"religion": "Christian", "care_style": "gentle"}

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

























    