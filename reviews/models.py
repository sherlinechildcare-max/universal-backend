from django.db import models
from users.models import CustomUser

class Review(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_reviews')
    caregiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} rated {self.caregiver}"