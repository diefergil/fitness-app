# Django
from django.contrib.auth.models import User
from django.db import models


class UserPayment(models.Model):
    user = models.ForeignKey(
        User,
        editable=False,
        on_delete=models.CASCADE,
    )
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500, blank=True, null=True)
