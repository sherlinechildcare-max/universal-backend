from django.db import models
from users.models import CustomUser

class Payment(models.Model):
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='payments_made'
    )
    caregiver = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='payments_received'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='paid')
    tip = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Payment: {self.client} → {self.caregiver}"